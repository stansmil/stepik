import json

from statistics.distribution import NormalDistribution


def get_z_params(val) -> tuple:
    M = 100
    sd = 15
    Z = NormalDistribution.Z(val, M, sd)
    precision = int((Z * 100) % 10)
    Z = round((Z - precision / 100), 2)
    return Z, precision


def get_table_possibilities(Z):
    """Будьте аккуратны при использовании этих таблиц: часто для интересующего нас z-значения
    указывается процент наблюдений, который не превосходит указанное z-значение."""
    table_datafile = "../data/right_std_normal_probabilities.json" if Z > 0 else \
        "../data/left_std_normal_probabilities.json"
    with open(table_datafile, "r") as fp:
        return json.load(fp)


def calculate_possibility(val):
    """Какой приблизительно процент людей обладает IQ > 125?"""
    z, precision = get_z_params(val)
    tbl_poss = get_table_possibilities(z)
    possibility = None
    for possibilities in tbl_poss:
        if z in possibilities:
            possibility = possibilities[precision + 1]
            break

    answer = 100 - (int(possibility * 100))
    # print(f"{answer}%")
    return answer


def task1():
    """#Task1
    Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение
    со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15)."""
    return calculate_possibility(125)


def task2():
    """#Task2
    Какой приблизительно процент людей обладает IQ на промежутке от 70 до 112"""
    return calculate_possibility(70) - calculate_possibility(112)


print(task1())
print(task2())
