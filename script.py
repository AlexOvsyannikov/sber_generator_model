#!/usr/bin/env python
# -*- coding: utf-8 -*-

import api

sber_api = api.SberApi()
text = input()

try:
    prediction = sber_api.get_prediction(text)
    print(prediction)
except Exception as e:
    print("Произошла ошибка, возможно, в тексте есть нечитаемые символы")
    print(e)

