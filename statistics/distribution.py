import math

from data import possibility_tables


def Z(avg_partial, avg_general, sd):
        """

        :param avg_partial:
        :param avg_general:
        :param sd: standard deviation
        :return:
        """
        return round((avg_partial - avg_general) / sd, 2)


def standard_deviation(disp):
        """"
        :param disp: variance (dispersion)
        """
        return round(math.sqrt(disp), 2)


def standard_error_of_mean(sd, n):
        """

        :param sd: standard deviation
        :param n: amount elements
        :return:
        """
        return round(sd / math.sqrt(n), 2)


def calculate_possibility(val, M, sd):
    z, precision = get_z_possibility_params(val, M, sd)
    tbl_poss = possibility_tables.possibilities_right if z > 0 else possibility_tables.possibilities_left
    possibility = None
    for possibilities in tbl_poss:
        if z in possibilities:
            possibility = possibilities[precision + 1]
            break

    answer = 100 - (int(possibility * 100))
    # print(f"{answer}%")
    return answer


def get_z_possibility_params(val, M, sd) -> tuple:
    Zi = Z(val, M, sd)
    hundred_prec = int((Zi * 100) % 10)
    return round(Zi, 1), hundred_prec
