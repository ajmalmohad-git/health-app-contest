from flask import Flask , render_template , request, redirect

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

if __name__ == "__main__":
    app.run(debug=True)
