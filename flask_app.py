# app.py
from flask import Flask, render_template, request
from model import DecisionTreeClassifier, regressor_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def diabeties_view():
    if request.method == 'GET':
        return render_template("diabeties.html")
    elif request.method == 'POST':
        glu = float(request.form["Glucose"])
        bp = float(request.form["BloodPressure"])
        st = float(request.form["SkinThickness"])
        ins = float(request.form["Insulin"])
        bmi = float(request.form["BMI"])
        pg = float(request.form["Pregnancies"])
        age = float(request.form["Age"])
        dpf = float(request.form["DiabetesPedigreeFunction"])

        op_array = regressor_model.predict([[glu, bp, st, ins, bmi, pg, age, dpf]])
        y_pred = round(op_array[0], 2)
        return render_template("result.html", predicted_price=y_pred)


if __name__ == '__main__':
    app.run(debug=True)