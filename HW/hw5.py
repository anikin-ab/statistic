# 1)
t_k = 'Стьюдента используется: не известна сигма ген совокупности; ' \
    'нормальном распределении; ' \
    'равенстве дисперсий'
Z_k = 'при нормальном распределении' \
    'известна сигма ген совокупности'



# ЗАДАЧА №2
#Проведите тест гипотезы. Утверждается, что шарики
#для подшипников, изготовленные автоматическим станком,
# имеют средний диаметр 17 мм. Используя односторонний
# критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100
# шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна
# и равна 4 кв. мм.
import numpy as np
# from scipy import stats
import requests
import pylab
import scipy.stats as stats


def task1():
    X = 17.5
    mu = 17
    a = 0.05
    n = 100
    D_x = 4
    sigma = 2 # используем Z-критерий
    # H0: D = 17; H_a: D != 17
    v = 1.984
    Z = (X - mu)/(sigma/np.sqrt(n))
    print(Z) # Z = 2.5
    if Z < v: print("H0 is correct, D = 17mm")
    else: print("H0 uncorrect, D != 17mm")

task1()

# ЗАДАЧА №3
# 3.Проведите тест гипотезы. Продавец утверждает, что средний вес
# пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что
# доверительная вероятность равна 99%? (Провести двусторонний тест.)

def task2():
    x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
    n = len(x)
    M_X = 200

    p = 0.99
    a = 1 - p
    sigma = 0 # используем t-критерий
    print('n = ', n) # n = 10
    mu = np.mean(x)
    print('mu = ', mu) # = 198.5
    sigma = np.std(x, ddof=1)
    print('sigma = ', sigma) # 4.453463071962462

    t = (M_X - mu) / (sigma / np.sqrt(n))
    print('t = ', t) # t = 1.065
    T_t = 2.821
    H0 = 'средний вес пачки печенья = 200гр'
    H_a = 'средний вес пачки печенья НЕ = 200гр'

    # print(stats.ttest_1samp(x, mu)) # TtestResult(statistic=0.0, pvalue=1.0, df=9)

    print('\nОдносторонний тест')
    if t < T_t: print("t попадает в область принятия H0, H0 верна")
    else: print("t не попадает в область принятия H0, H0 не верна \n")

    #двусторонний тест
    a1 = a / 2
    # print('a1 = ', a1) # = 0.005
    P1 = 1 - a1
    # print('P1 = ', P1) # 0.995
    T_t2 = 4.781
    print("\nДвусторонний тест:")
    print('a1 = ', a1)
    print('P1 = ', P1)

    if t < T_t2:
        print(f"{t} < {T_t2}, t попадает в область принятия H0, H0 верна")
        print(H0)
    else:
        print(f"{t} > {T_t2}, t не попадает в область принятия H0, H0 не верна")
        print(H_a)

# task2()
