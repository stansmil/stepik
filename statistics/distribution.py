import math


class NormalDistribution:

    @staticmethod
    def Z(val, avg, deviation):
        return round((val - avg) / deviation, 2)

    @staticmethod
    def standard_deviation(disp):
        """"
        :param disp: variance (dispersion)
        """
        return math.sqrt(disp)

    @staticmethod
    def standard_error_of_mean(sd, n):
        """

        :param sd: standard deviation
        :param n: amount elements
        :return:
        """
        return sd / math.sqrt(n)
