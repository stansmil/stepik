from statistics.distribution import calculate_possibility


def task1():
    """#Task1
    Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение
    со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15)."""
    return calculate_possibility(125, M=100, sd=15)


def task2():
    """#Task2
    Какой приблизительно процент людей обладает IQ на промежутке от 70 до 112"""
    return calculate_possibility(77, M=100, sd=15) - calculate_possibility(112, M=100, sd=15)


print(task2())
