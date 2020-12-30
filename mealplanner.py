import csv
import math
from flask import Flask
app = Flask(__name__)

@app.route('/')

class Food(object):
    # constructor with default values
    def __init__ (self, name, foodgroup, calories, fat, protein, carbs):
        self.name = name
        self.foodgroup = foodgroup
        self.calories = calories
        self.fat = fat
        self.protein = protein
        self.carbs = carbs

def breakfastcruncher(masterlist):
    breakfastlist = []
    incomplete = True
    while incomplete == True:
        user_entry = 1
        food = input("Enter a breakfast item:")
        for x in masterlist:
            if x.name == food:
                breakfastlist.append(x)
                user_entry = 0
        if user_entry == 1:
            print("We couldn't find your food in our database - please enter the nutrition facts!")
            foodgroup = input("Enter the group of food your food is in:")
            calories = int(input("Enter the number of calories in the food:"))
            fat = float(input("Enter the grams of fat in the food:"))
            protein = float(input("Enter the grams of protein in the food:"))
            carbs = float(input("Enter the grams of carbs in the food:"))
            newfood = Food(food,foodgroup,calories,fat,protein,carbs)
            breakfastlist.append(newfood)
            writer(newfood)

        incomplete_num = int(input("Enter 0 to add another food and 1 to move on:"))
        if incomplete_num == 1:
            incomplete = False

    return breakfastlist

def linnercruncher(masterlist):
    linnerlist = []
    incomplete = True
    while incomplete == True:
        user_entry = 1
        food = input("Enter a lunch/dinner item:")
        for x in masterlist:
            if x.name == food:
                linnerlist.append(x)
                user_entry = 0
        if user_entry == 1:
            print("We couldn't find your food in our database - please enter the nutrition facts!")
            foodgroup = input("Enter the group of food your food is in:")
            calories = int(input("Enter the number of calories in the food:"))
            fat = float(input("Enter the grams of fat in the food:"))
            protein = float(input("Enter the grams of protein in the food:"))
            carbs = float(input("Enter the grams of carbs in the food:"))
            newfood = Food(food,foodgroup,calories,fat,protein,carbs)
            linnerlist.append(newfood)
            writer(newfood)

        incomplete_num = int(input("Enter 0 to add another food and 1 to move on:"))
        if incomplete_num == 1:
            incomplete = False

    return linnerlist

def snackcruncher(masterlist):
    snacklist = []
    incomplete = True
    while incomplete == True:
        user_entry = 1
        food = input("Enter a snack:")
        for x in masterlist:
            if x.name == food:
                snacklist.append(x)
                user_entry = 0
        if user_entry == 1:
            print("We couldn't find your food in our database - please enter the nutrition facts!")
            foodgroup = input("Enter the group of food your food is in:")
            calories = int(input("Enter the number of calories in the food:"))
            fat = float(input("Enter the grams of fat in the food:"))
            protein = float(input("Enter the grams of protein in the food:"))
            carbs = float(input("Enter the grams of carbs in the food:"))
            newfood = Food(food,foodgroup,calories,fat,protein,carbs)
            snacklist.append(newfood)
            writer(newfood)

        incomplete_num = int(input("Enter 0 to add another food and 1 to move on:"))
        if incomplete_num == 1:
            incomplete = False

    return snacklist

def reader():
    master = []
    with open('myproject/MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.csv', encoding ="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)
        for row in csv_reader:
            entry = Food(row[1],row[2],int(float(row[3])),float(row[4]),float(row[5]),float(row[6]))
            master.append(entry)
    return master

def writer(newfood):
    with open('myproject/MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.csv', "a+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['',newfood.name,newfood.foodgroup,newfood.calories,newfood.fat,newfood.protein,newfood.carbs])

def dailybreakdown(calorie_target,fat_target,protein_target,carbs_target):
    fat_grams = calorie_target * fat_target / 9
    protein_grams = calorie_target * protein_target / 4
    carbs_grams = calorie_target * carbs_target / 4

    return fat_grams,protein_grams,carbs_grams

def mealcreater(calorie_target,fat_target,protein_target,carbs_target,breakdown,meallist,meal):
    if meal == "breakfast":
        mult = .2
        targ_score = 13
    elif meal == "lunch" or meal == "dinner":
        mult = .35
        targ_score = 20
    else:
        mult = .1
        targ_score = 10
    meal_calories = mult * calorie_target
    meal_fat = mult * breakdown[0]
    meal_protein = mult * breakdown[1]
    meal_carbs = mult * breakdown[2]
    possible_meals = []
    for x in meallist:
        quantity = 1
        while meal_calories - (quantity*float(x.calories)) > 50:
            quantity += 1
        food_score = 0
        cal_score = (abs((quantity*float(x.calories)) - meal_calories) / 100) # 100 calories off is okay
        fat_score = (abs((quantity*float(x.fat)) - meal_fat) * fat_target) # 100 calories off is okay
        protein_score = (abs((quantity*float(x.protein)) - meal_protein) * protein_target)
        carbs_score = (abs((quantity*float(x.carbs)) - meal_carbs) * carbs_target)
        food_score = cal_score + fat_score + protein_score + carbs_score
        if food_score < targ_score:
            possible_meals.append([x,quantity])

            #if len(possible_breakfasts) < 2:
    #    recommend(masterlist,'breakfast',calorie_target,fat_target,protein_target,carbs_target)
    return possible_meals

def output(foodlist,meal):
    print(meal, "options for today:")
    print('-----------')
    for x in foodlist:
        print(x[1],"servings of",x[0].name,':',round(x[0].calories*x[1],1),"calories,",round(x[0].fat*x[1],1),"g fat,",round(x[0].protein*x[1],1),"g protein,",round(x[0].carbs*x[1],1),"g carbs")
    print()

#Go through masterlist and find 2 foods that are close to the calorie and macros target for the meal
def recommend(masterlist,foodtype,calorie_target,fat_target,protein_target,carbs_target):
    pass

'''def main():
    # Read in Food data and create master list of food objects and macros
    #global masterlist
    #masterlist = reader()

    # Ask user which breakfast items they have - if not present in masterlist, ask them for breakdown (add to masterlist and write into csv)
    # Given the user foods, create a list with Food objects called "Breakfast"
    #breakfastlist = breakfastcruncher(masterlist)

    #Below is a hardcoded testcase to save time while debugging
    breakfastlist = []
    lunchlist = []
    dinnerlist = []
    snacklist = []
    for x in masterlist:
        if x.name == "cereal" or x.name == "waffles" or x.name == "eggs" or x.name == "Bagels Wheat":
            breakfastlist.append(x)
        if x.name == "Corn Fritter" or x.name == "Artichokes Stuffed" or x.name == "Ratatouille" or x.name == "Cooked Trout" or x.name == "Cooked Sturgeon" or x.name == "Soy Protein Isolate Potassium Type" or x.name == "Beef Round Top Round Roast Boneless Separable Lean And Fat Trimmed To 0 Inch Fat Select Cooked Roasted" or x.name == "Bacon (Pan-Fried)":
            lunchlist.append(x)
        if x.name == "Bagels Wheat" or x.name == "Restaurant Mexican Refried Beans" or x.name == "Pork Spare Ribs" or x.name == "Boston Steak (Pork)" or x.name == "Country-Style Roasted Pork Ribs" or x.name == "Dennys Golden Fried Shrimp" or x.name == "Papad" or x.name == "Roasted Pork Backribs" or x.name == "Cooked Artichokes (Globe Or French)" or x.name == "Beef Grass-Fed Ground Raw":
            dinnerlist.append(x)
        if x.name == "Nuts Mixed Nuts Dry Roasted With Peanuts With Salt Added" or x.name == "Baby Carrots" or x.name == "Sun-Dried Tomatoes" or x.name == "Sweet Potato Canned Vacuum Pack" or x.name == "Cooked Soybean Sprouts" or x.name == "Babyfood Dessert Blueberry Yogurt Strained" or x.name == "Crackers Cheese Reduced Fat" or x.name == "Raspberries Frozen Red Sweetened" or x.name == "Snacks Pretzels Hard Plain Salted":
            snacklist.append(x)
    calorie_target = 2000
    fat_target = .25
    protein_target = .25
    carbs_target = .5
    # Ask user which lunch/dinner items they have - if not present in masterlist, ask them for breakdown (add to masterlist and write into csv)
    # Given the user foods, create a list with Food objects called "Lunch/Dinner"
    #lunchdinnerlist = linnercruncher(masterlist)

    # Ask user which snacks/desserts they have - if not present in masterlist, ask them for breakdown (add to masterlist and write into csv)
    # Given the user foods, create a list with Food objects called "Snacks/Desserts"
    #snacklist = snackcruncher(masterlist)

    # Ask user for calorie goal and desired macro percentage breakdown
    calorie_target = int(input("Enter your calorie goal:"))
    fat_target = float(input("Enter your target fat breakdown (as a decimal):"))
    protein_target = float(input("Enter your target protein breakdown (as a decimal):"))
    carbs_target = float(input("Enter your target carbs breakdown (as a decimal):"))
    while fat_target + protein_target + carbs_target != 1:
        print("Your macro breakdown doesn't add up - sum of all target should be 1 (100%)")
        fat_target = float(input("Enter your target fat breakdown (as a decimal):"))
        protein_target = float(input("Enter your target protein breakdown (as a decimal):"))
        carbs_target = float(input("Enter your target carbs breakdown (as a decimal):"))

    # Based on user's calorie goal and macro breakdown, split up how many calories they should get from breakfast/lunch/dinner/snacks
    breakdown = dailybreakdown(calorie_target,fat_target,protein_target,carbs_target)
    breakfast_calories = .2 * breakdown
    lunch_calories = .35 * breakdown
    dinner_calories = .35 * breakdown
    snack_calories = .1 * breakdown

    # Go through and create 5 sets of meals for 5 days
    breakfastplan = mealcreater(calorie_target,fat_target,protein_target,carbs_target,breakdown,breakfastlist,"breakfast")
    lunchplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, lunchlist,"lunch")
    dinnerplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, dinnerlist,"dinner")
    snackplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, snacklist,"snack")
    output(breakfastplan,"breakfast")
    output(lunchplan,"lunch")
    output(dinnerplan,"dinner")
    output(snackplan,"snack")

    # Do not repeat the same meal in the next two days - if you have to, tell user they should try to diversify their breakfast or lunch/dinner

    #If user's meals don't meet required breakfast/lunch/dinner minimums, tell user they should pick healthier options and provide 2-3 examples from masterlist that do

main()'''