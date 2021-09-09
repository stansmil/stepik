from statistics.distribution import NormalDistribution

"""
Рассчитайте 99% доверительный интервал для следующего примера:
xˉ=10 sd=5 n=100
"""

koeff_for_99 = 2.58
mean = 10
sd = 5
n = 100
standard_error = NormalDistribution.standard_error_of_mean(sd, n)

low_th = mean - koeff_for_99 * standard_error
high_th = mean + koeff_for_99 * standard_error
print(f"Trust interval 99% is: {low_th, high_th}")

"""
Рассчитайте 95% доверительный интервал для следующего примера:
xˉ=18.5 sd=4 n=64
"""

koeff_for_95 = 1.96
mean = 18.5
sd = 4
n = 64
standard_error = NormalDistribution.standard_error_of_mean(sd, n)

low_th = mean - koeff_for_95 * standard_error
high_th = mean + koeff_for_95 * standard_error
print(f"Trust interval 95% is: {low_th, high_th}")

