# Однофакторный дисперсионный анализ
from statistics import total_mean, mean


def sst(groups: list):
    """
    Sum Squares Total

    :param groups:
    :return:
    """
    mean =total_mean(groups)
    groups_vals = []
    [groups_vals.extend(g) for g in groups]
    return round(sum([(v - mean)**2 for v in groups_vals]), 2)


def ssb(groups: list):
    """
    Sum Squares between groups

    :return:
    """
    tm = total_mean(groups)
    return round(sum((len(g) * (mean(g) - tm)**2) for g in groups), 2)


def ssw(groups: list) -> float:
    """
    Sum Squares within groups

    :param groups:
    :return:
    """
    ssg = []
    for g in groups:
        gm = mean(g)
        ssg.append(sum((v - gm)**2 for v in g))

    return round(sum(ssg), 2)
