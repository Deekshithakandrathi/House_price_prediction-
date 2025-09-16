from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load ML model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Prediction page
@app.route("/predict_page")
def predict_page():
    return render_template("predict.html")

# Prediction result
@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_input = np.array([features])
    prediction = model.predict(final_input)[0]
    return render_template("predict.html", prediction_text=f"Estimated Price: ${prediction:,.2f}")

if __name__ == "__main__":
    app.run(debug=True)
