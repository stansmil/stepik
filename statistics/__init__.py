import math


def mean(vals: list) -> float:
    return round(sum(vals) / len(vals), 2)


def total_mean(groups: list) -> float:
    return round(sum(mean(g) for g in groups) / len(groups), 2)


def correlation_koef(coords: list):
    xx = (c[0] for c in coords)
    yy = (c[1] for c in coords)
    avg_x = sum(xx) / len(coords)
    avg_y = sum(yy) / len(coords)
    return round(sum((c[0] - avg_x) * (c[1] - avg_y) for c in coords) / math.sqrt(sum((x - avg_x) for x in xx)**2 * sum((y - avg_y) for y in yy)**2), 2)
