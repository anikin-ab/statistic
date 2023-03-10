# линейная регрессия
import numpy as np


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])# зарплата
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832]) #кредит скоринш
n = len(zp) #10
# print('n=', len(zp), len(ks))
# x = zp
# y = ks
# print(x, y)


# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового
# балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.
def task1():
    ' Используя математические операции, посчитать коэффициенты линейной регрессии,'

    x = zp
    y = ks
    b1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x ** 2) - np.sum(x) ** 2)
    b0 = np.mean(y) - b1 * np.mean(x)
    print(f'b1 = {b1} \nb0 = {b0}') # КОЭФ b1 = 2.62053 b0 = 444.1773
    y_pred1 = b0 + b1 * x
    print(y_pred1)
    # [535.89621821 562.10160703 942.07974498 968.2851338  548.99891262
    #  627.61507909 585.68645697 837.25818968 758.64202321 732.43663439]

    # ANSWER: КОЭФ b1 = 2.62053 b0 = 444.1773


# task1()

def task1_2():
    'matrix method'
    x = zp.reshape(n, 1)  # ПРЕОБРАЗОВЫВАЕМ В ВЕКТОР-СТОЛБЕЦ
    y = ks.reshape(n, 1)
    X = np.hstack([np.ones((n, 1)), x])  # доб 8 единиц к матрице х
    B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
    Bc = np.array(B.reshape((1, -1)))
    print(f'b0 = {Bc[0, 0]}, b1 = {Bc[0, 1]}')
    # ANSWER: b0 = 444.17735732435943, b1 = 2.620538882402764

# task1_2()

#Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).
def task2():
    B1 = 2.620538882402764
    x = zp
    y = ks
    alpha = 1e-6  # скорость обучения
    for i in range(10):
      B1 -= alpha * (2/n) * np.sum((B1 * x - y) * x)
      print('B1 = {}'.format(B1))

    # ОТВЕТ
    # B1 = 2.710618050468144
    # B1 = 2.798215249199985
    # B1 = 2.883398864795728
    # B1 = 2.9662353991942383
    # B1 = 3.0467895219931598
    # B1 = 3.125124120935778
    # B1 = 3.20130035100681
    # B1 = 3.2753776821754492
    # B1 = 3.347413945822933
    # B1 = 3.4174653798908845


# task2()
# ЗАДАЧА 3. Произвести вычисления как в пункте 2, но с вычислением intercept
def task3():
    B1 = 2.620538882402764
    x = zp
    y = ks
    alpha = 1e-6  # скорость обучения
    for i in range(10):
        B1 -= alpha * (2 / n) * np.sum((B1 * x - y) * x)
        B0 = np.mean(y) - B1 * np.mean(x)
        print(f'B1 = {B1}, B0 = {B0}')

    # Учесть, что изменение коэффициентов должно производиться на каждом шаге
    # одновременно (то есть изменение одного коэффициента не должно влиять
    # на изменение другого во время одной итерации). - НЕ ОЧЕНЬ ПОНЯТНО УСЛОВИЕ
    def mse_(B1, y=y, x=x, n=8):
        return np.sum((B1 * x - y) ** 2) / n  # находим среднеквадратичную ошибку
    # B1 = 2.710618050468144, B0 = 435.04332968253016
    # B1 = 2.798215249199985, B0 = 426.1609737311215
    # B1 = 2.883398864795728, B0 = 417.5233551097131
    # B1 = 2.9662353991942383, B0 = 409.1237305217042
    # B1 = 3.0467895219931598, B0 = 400.95554246989354
    # B1 = 3.125124120935778, B0 = 393.0124141371121
    # B1 = 3.20130035100681, B0 = 385.28814440790944
    # B1 = 3.2753776821754492, B0 = 377.7767030274094
    # B1 = 3.347413945822933, B0 = 370.4722258935546
    # B1 = 3.4174653798908845, B0 = 363.3690104790643


    for i in range(1000):
        B1 -= alpha * (2 / n) * np.sum((B1 * x - y) * x)
        B0 = np.mean(y) - B1 * np.mean(x)
        if i % 100 == 0:
            print('Iteration = {i}, B1 = {B1}, B0 = {B0}, mse = {mse}'.format(i=i, B1=B1, B0=B0, mse=mse_(B1)))
    # Iteration = 0, B1 = 3.485586672785675, B0 = 356.4615113795325, mse = 170187.86155719575
    # Iteration = 100, B1 = 5.742737635652006, B0 = 127.58640374488652, mse = 71018.61545400636
    # Iteration = 200, B1 = 5.88082239923956, B0 = 113.58460871710861, mse = 70647.46728699603
    # Iteration = 300, B1 = 5.88926995203896, B0 = 112.7280268632494, mse = 70646.07823779692
    # Iteration = 400, B1 = 5.889786744380452, B0 = 112.67562411982203, mse = 70646.07303917856
    # Iteration = 500, B1 = 5.88981835996553, B0 = 112.67241829949512, mse = 70646.07301972236
    # Iteration = 600, B1 = 5.88982029409872, B0 = 112.6722221783898, mse = 70646.07301964951
    # Iteration = 700, B1 = 5.889820412422362, B0 = 112.67221018037242, mse = 70646.07301964927
    # Iteration = 800, B1 = 5.889820419660998, B0 = 112.67220944637472, mse = 70646.07301964927
    # Iteration = 900, B1 = 5.889820420103832, B0 = 112.67220940147138, mse = 70646.07301964925



task3()


