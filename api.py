#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


class SberApi:
    """Класс для общения с API модели"""
    def __init__(self):
        self.link = 'https://api.aicloud.sbercloud.ru/public/v1/public_inference/gpt3/predict'

    def get_prediction(self, text):
        data = {"title": "Затравка", "text": text}
        answer = requests.post(url=self.link, json=data)
        to_dict = json.loads(answer.text)
        prediction = to_dict.get("predictions", 0)

        if prediction:
            return prediction
        else:
            raise Exception
