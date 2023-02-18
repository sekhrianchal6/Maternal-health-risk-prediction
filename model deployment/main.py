import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pk1", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    features = [x for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    if prediction == [3.0]:
        prediction = "high"
    elif prediction == [2.0]:
        prediction = "mid "
    else:
        prediction = "low"

    return render_template('index.html', prediction_text=f"The risk level is {prediction}")


if __name__ == "__main__":
    app.run(debug=True)
