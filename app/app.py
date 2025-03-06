from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from model import load_model  # Import your ML model function

app = Flask(__name__)

# Load the trained model
model = load_model()

# Home route with input form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Extract data from form
            data = [
                float(request.form["Pregnancies"]),
                float(request.form["Glucose"]),
                float(request.form["BloodPressure"]),
                float(request.form["SkinThickness"]),
                float(request.form["Insulin"]),
                float(request.form["BMI"]),
                float(request.form["DiabetesPedigreeFunction"]),
                float(request.form["Age"])
            ]

            # Make prediction
            prediction = model.predict([data])[0]  # Assuming model.predict() returns an array

            # Display result
            result = "Diabetic" if prediction == 1 else "Non-Diabetic"
            return render_template("index.html", prediction=result)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

