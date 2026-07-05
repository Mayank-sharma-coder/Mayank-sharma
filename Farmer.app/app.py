from flask import Flask, render_template
import numpy as np
import pickle
from flask import request

app = Flask(__name__)
crop_model = pickle.load(open('./models/best_modelrandom_forest_model.pkl', 'rb'))
crop_encoder = pickle.load(open('./models/crop_label_encoder.pkl', 'rb'))
crop_scaler = pickle.load(open('./models/standard_scaler.pkl', 'rb'))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crop",methods=["GET","POST"])
def crop():
    if request.method== "POST":
       return "POST Working"
    return render_template("crop.html")

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

if __name__ == "__main__":
    app.run(debug=True)