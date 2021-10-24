#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import api
import extra_classes

app = Flask(__name__)
sber_api = api.SberApi()
logger = extra_classes.Logger()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    text = request.form.get("text")
    try:
        prediction = sber_api.get_prediction(text)
        logger.log({"text": text,
                    "prediction": prediction})

        return render_template("prediction.html", text=prediction)
    except:
        return render_template("prediction.html", text="Произошла ошибка, возможно, в тексте есть нечитаемые символы")


if __name__ == '__main__':
    app.run()