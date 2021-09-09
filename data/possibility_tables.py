import os
import json

"""Будьте аккуратны при использовании этих таблиц: часто для интересующего нас z-значения
указывается процент наблюдений, который не превосходит указанное z-значение."""

dir_path = os.path.dirname(__file__)
fp = open(os.path.join(dir_path, "right_std_normal_possibilities.json"), "r")
possibilities_right = json.load(fp)
fp = open(os.path.join(dir_path, "left_std_normal_possibilities.json"), "r")
possibilities_left = json.load(fp)
fp.close()
