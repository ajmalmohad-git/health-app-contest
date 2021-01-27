from flask import Flask, render_template,request,jsonify
from bmi import Meal_bmi
from calories_check import req
import json


app = Flask(__name__)

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
			return render_template('home.html',data = json.dumps(data))
			
@app.route('/<name>')
def calories(name):

	info = req(name)

	print(info)
	data = {
	"inna" : info
	}

	return json.dumps(data["inna"])



if __name__ == "__main__" :
	app.run(debug=True)

