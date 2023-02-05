import scipy.stats as stats

H0 = 'Принимается нулевая гипотеза, различий нет'
H1 = 'Принимается альтернативная гипотеза, различия есть'

# ЗАДАЧА №1
#Выберете тест и проверьте, есть ли различия между выборками:
# 1 ) Даны две независимые выборки. Не соблюдается условие нормальности

def task1():
    x1 = [380, 420, 290]
    y1 = [140, 360, 200, 900]
    a = 0.05
    # Mann-Whitney
    st, pv = stats.mannwhitneyu(x1, y1)
    print(st, pv)
    MW = stats.mannwhitneyu(x1, y1)
    print(MW)
    # MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
    if pv > a:
        print(round(pv, 3), '>', a)
        print(H0)
    else:
        print(round(pv, 3), '<', a)
        print(H1)

    # ANSWER: 0.629 > 0.05
    # Принимается нулевая гипотеза, различий нет
task1()

# ЗАДАЧА 2
#2 ) Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата, потом через 10 минут
# и через 30 минут. Есть ли статистически значимые различия?
def task2():
    x1 = [150, 160, 165, 145, 155]
    x2 = [140, 155, 150, 130, 135]
    x3 = [130, 130, 120, 130, 125]
    a = 0.05
    # Friedman
    st, pv = stats.friedmanchisquare(x1, x2, x3)
    print(st, pv)
    FR = stats.friedmanchisquare(x1, x2, x3)
    print(FR)
    # FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)
    if pv > a:
        print(round(pv, 3), '>', a)
        print(H0)
    else:
        print(round(pv, 3), '<', a)
        print(H1)

    # ANSWER: 0.008 < 0.05
    # Принимается альтернативная гипотеза, различия есть
# task2()

# ЗАДАЧА 3
# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было
def task3():
    x1 = [150, 160, 165, 145, 155]
    x2 = [140, 155, 150, 130, 135]
    a = 0.05
    # Уилкоксон
    st, pv = stats.wilcoxon(x1, x2)
    print(st, pv)
    WL = stats.wilcoxon(x1, x2)
    print(WL)
    # WilcoxonResult(statistic=0.0, pvalue=0.0625)
    if pv > a:
        print(round(pv, 3), '>', a)
        print(H0)
    else:
        print(round(pv, 3), '<', a)
        print(H1)
    # ANSWER: 0.062 > 0.05
    # Принимается нулевая гипотеза, различий нет
# task3()

# ЗАДАЧА 4
# Даны 3 группы учеников плавания.
def task4():
    x1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
    x2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
    x3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]
    a = 0.05
    # Крускал-Уоллис
    st, pv = stats.kruskal(x1, x2, x3)
    print(st, pv)
    KW = stats.kruskal(x1, x2, x3)
    print(KW)
    # KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)
    if pv > a:
        print(round(pv, 3), '>', a)
        print(H0)
    else:
        print(round(pv, 3), '<', a)
        print(H1)
    # ANSWER: 0.065 > 0.05
    # Принимается нулевая гипотеза, различий нет
# task4()

# задача 5
# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному
# закону распределения. Объем выборки 10, уровень статистической значимости 5%

def task5():
    import numpy as np
    x = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
    n = len(x)
    M_X = 2.5
    a = 0.05
    sigma = 0  # используем t-критерий
    print('n = ', n)  # n = 10
    mu = np.mean(x)
    print('mu = ', mu)  # mu =  2.52
    sigma = np.std(x, ddof=1)
    print('sigma = ', round(sigma, 3))  #sigma =  0.157

    t = (mu - M_X) / (sigma / np.sqrt(n))
    print('t = ', round(t, 3))  # t =  -0.563
    T_t = 1.833
    Ts, pv = stats.ttest_1samp(x, M_X) #TtestResult(statistic=0.5630613661802959, pvalue=0.5871439993940629, df=9)
    print('Ts', round(Ts, 3), 'pv', round(pv, 3)) #t =  0.563;  pv=0.587
    print('\nОдносторонний тест')
    if t < T_t:
        print(f"{t} < {T_t}, t попадает в область принятия H0, H0 верна")
        print("M_X =", M_X)
    else:
        print(f"{t} > {T_t}, t не попадает в область принятия H0, H0 не верна")
        print("M_X !=", M_X)
    if pv > a:
        print(round(pv, 3), '>', a, H0)
    else: print(round(pv, 3), '<', a, H0)
    # ANSWER: Односторонний тест
    # 0.5630613661802959 < 1.833, t попадает в область принятия H0, H0 верна
    # M_X = 2.5
    # 0.587 > 0.05 Принимается нулевая гипотеза, различий нет


    # двусторонний тест
    a1 = a / 2
    # print('a1 = ', a1) # = 0.005
    P1 = 1 - a1
    # print('P1 = ', P1) # 0.995
    T_t2 = 3.25
    print("\nДвусторонний тест:")
    print('a1 = ', a1) #a1 =  0.025
    print('P1 = ', P1)

    if t < T_t2:
        print(f"{t} < {T_t2}, t попадает в область принятия H0, H0 верна")
        print(H0)
    else:
        print(f"{t} > {T_t2}, t не попадает в область принятия H0, H0 не верна")
        print(H1)
    # ANSWER: Двухсторонний тест
    # 0.5630613661802959 < 3.25, t попадает в область принятия H0, H0 верна
    # M_X = 2.5

# task5()