from flask import Flask , render_template , request, redirect,jsonify
from bmi import Meal_bmi
from calories_check import req
import json

app = Flask(__name__)

def calccal(life,bmr):
    one = bmr*1.2
    two = bmr*1.375
    three = bmr*1.55
    four = bmr*1.725
    five = bmr*1.9
    if life == "1":
        return one
    elif life == "2":
        return two
    elif life == "3":
        return three
    elif life == "4":
        return four
    else:
        return five


@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/workout',methods=["GET","POST"])
def work():
    return render_template('workout.html')

@app.route('/workout/calorie',methods=["GET","POST"])
def calc():
    if request.method == "POST":
        if request.form['gender'] == 'male':
            life = request.form['lifestyle']
            bmr = (13.397*int(request.form['weight'])) +( 4.799*int(request.form['height'])) - (5.677*int(request.form['age'])) + 88.362
            calorie = round(calccal(life,bmr))
            calories = [calorie,round(calorie*0.90),round(calorie*0.79),round(calorie*0.59)]
            return render_template('calorie.html',calories=calories)
        else:
            life = request.form['lifestyle']
            bmr = (9.247*int(request.form['weight'])) +( 3.098*int(request.form['height'])) - (4.330*int(request.form['age'])) + 447.593
            calorie = round(calccal(life,bmr))
            calories = [calorie,round(calorie*0.90),round(calorie*0.79),round(calorie*0.59)]
            return render_template('calorie.html',calorie=calorie)
    else:
        return redirect('/workout')


#creating an instance
info = Meal_bmi()
print(info.finding_height_cm(167))
#main page
@app.route('/diet', methods=['GET','POST'])
def home():
	if request.method == 'GET' :
		data = {
		"synopsis" : ""}
		return render_template('diet_main.html',data = data)
	else :

		weight = request.form['weight']

		try :
			#extracting height and weight from user
			height = request.form['height']

			bmi_index = info.bmi(int(weight),height = int(height))
			meals = info.response_meal(bmi_index)

			data = {
			#"synopsis" : [bmi_index,meals]
			"synopsis" : [bmi_index,meals]
			}
			return render_template('home.html',data = json.dumps(data))

		except :	
			feet = request.form["feet"]
			inch = request.form["inch"]

			bmi_index = info.bmi(int(weight),ft = int(feet), inch = int(inch))
			meals = info.response_meal(bmi_index)
			data = {
			#"synopsis" : [bmi_index,meals]
			"synopsis" : [bmi_index,meals]
			}
			return render_template('diet_main.html',data = json.dumps(data))
			
@app.route('/<name>')
def calories(name):

	info = req(name)

	print(info)
	data = {
	"inna" : info
	}

	return json.dumps(data["inna"])


if __name__ == "__main__":
    app.run(debug=True)


