from flask import Flask,render_template,url_for,request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from mealplanner import breakfastcruncher,linnercruncher,snackcruncher,dailybreakdown,mealcreater
from flask_bootstrap import Bootstrap
import csv

def reader():
    master = []

    with open('MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.csv', 'r',encoding ="ISO-8859-1") as csv_file:
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
    with open('MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.csv', "a+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['',newfood.name,newfood.foodgroup,newfood.calories,newfood.fat,newfood.protein,newfood.carbs])

class Food(object):
    # constructor with default values
    def __init__ (self, name, foodgroup, calories, fat, protein, carbs):
        self.name = name
        self.foodgroup = foodgroup
        self.calories = calories
        self.fat = fat
        self.protein = protein
        self.carbs = carbs

global masterlist
masterlist = reader()
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

breakfastlist = []
lunchlist = []
dinnerlist = []
snacklist = []

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/target_request',methods=['GET','POST'])
def target_request():
    if request.method == 'POST':
        print("IT WORKED")
        global calorie_target, fat_target, protein_target, carbs_target
        calorie_target = float(request.form['caloriegoal'])
        fat_target = float(request.form["fatgoal"])
        carbs_target = float(request.form["carbsgoal"])
        protein_target = float(request.form["proteingoal"])
        print(calorie_target,fat_target)
        return render_template('target.html')
    else:
        return render_template('target.html')

@app.route('/foods',methods=['POST','GET'])
def foods():
    if request.method == 'GET':
        food = request.form['Food']
        mealtype = request.form['mealtype']
        print(food,mealtype)
        temp_food = None
        for x in masterlist:
            if food == x.name:
                temp_food = Food(x.name,mealtype,x.calories,x.fat,x.protein,x.carbs)
        if temp_food == None:
            return redirect('/addfoods.html')
        elif mealtype == 'breakfast':
            breakfastlist.append(temp_food)
        elif mealtype == 'lunch':
            lunchlist.append(temp_food)
        elif mealtype == 'dinner':
            dinnerlist.append(temp_food)
        elif mealtype == 'snack':
            snacklist.append(temp_food)
        return render_template("foods.html")
    else:
        return render_template("foods.html")

@app.route('/addfoods', methods=['POST', 'GET'])
def addfoods():
    if request.method == 'GET':
        name = request.form['food']
        mealtype = request.form['mealtype']
        cals = request.form["calories"]
        fat = request.form["fat"]
        protein = request.form["protein"]
        carbs = request.form["carbs"]
        newfood = Food(name,mealtype,cals,fat,protein,carbs)
        if mealtype == 'breakfast':
            breakfastlist.append(newfood)
        elif mealtype == 'lunch':
            lunchlist.append(newfood)
        elif mealtype == 'dinner':
            dinnerlist.append(newfood)
        elif mealtype == 'snack':
            snacklist.append(newfood)
        masterlist.append(newfood)
        writer(newfood)
        return redirect('/foods')
    else:
        return render_template('addfoods.html')

@app.route('/mealplan', methods=['POST', 'GET'])
def mealplan():
    breakdown = dailybreakdown(calorie_target, fat_target, protein_target, carbs_target)
    breakfastplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, breakfastlist,"breakfast")
    lunchplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, lunchlist, "lunch")
    dinnerplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, dinnerlist, "dinner")
    snackplan = mealcreater(calorie_target, fat_target, protein_target, carbs_target, breakdown, snacklist, "snack")
    return render_template('mealplan.html')


if __name__ == "__main__":
    app.run(debug=True)