"""
Рассчитайте 99% доверительный интервал для следующего примера:
xˉ=10 sd=5 n=100
"""
from statistics.distribution import NormalDistribution

koeff_for_99 = 2.58
mean = 10
sd = 5
n = 100
standard_error = NormalDistribution.standard_error_of_mean(sd, n)

low_th = mean - koeff_for_99 * standard_error
high_th = mean + koeff_for_99 * standard_error

print(f"Trust interval is: {low_th, high_th}")
