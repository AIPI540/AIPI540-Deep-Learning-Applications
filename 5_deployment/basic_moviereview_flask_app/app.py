from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/classify", methods=['POST'])
def classify():
    model = pickle.load(open('./models/model.pkl','rb'))
    vect = pickle.load(open('./models/vect.pkl','rb'))
    # Get the review from the form
    new_review = request.form['review']
    # Generate prediction
    y, proba = predict(new_review, model, vect)
    return render_template('display_result.html', review=new_review, prediction='Predicted sentiment: {}'.format(y), probability='Probability: {:.0%}'.format(proba))
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
