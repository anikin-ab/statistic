# Провести дисперсионный анализ для определения того,
# есть ли различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов. Даны значения роста в трех группах
# случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

# тест Шапиро
# множ сравнения, независ выборки - Курскала-Уоллиса
# одновыборочный тест


import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

def test1():
    f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
    h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
    sh = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
    print(f'len f, h, sh: {len(f)}, {len(h)}, {len(sh)}')# 8, 9, 11
    alpha = 0.05

    # ПРОВЕРКА НА НОРМАЛЬНОСТЬ
    f_Shapiro = stats.shapiro(f)
    h_Shapiro = stats.shapiro(h)
    sh_Shapiro = stats.shapiro(sh)
    print(f_Shapiro) # ShapiroResult(statistic=0.9775082468986511, pvalue=0.9495404362678528)
    print(h_Shapiro) # ShapiroResult(statistic=0.9579196572303772, pvalue=0.7763139009475708)
    print(sh_Shapiro) # ShapiroResult(statistic=0.9386808276176453, pvalue=0.5051165223121643)
    # RESULT:
    ### у трех выборок - нормальное распределение, Pvalue > alpha

    # МНОЖЕСТВЕННЫЕ СРАВНЕНИЯ НЕЗАВИС ВЫБОРОК
    # ТЕСТ ГИПОТЕЗЫ Н0 - РАЗЛИЧИЯ В СРЕДНЕМ РОСТЕ МЕЖДУ ВЫБОРКАМИ ОТСУТСВУЕТ
    # ТЕСТ КРУСКА-УОЛЛЕСА

    Krusk_test = stats.kruskal(f, h, sh)
    print(Krusk_test) # KruskalResult(statistic=7.897493213863828, pvalue=0.01927885061595347)
    # RESULT: Pvalue < alpha: отвергаем нулевую гипотезу = различия в среднем росте ЕСТЬ

    # ПРОВЕРКА НА ОДНОРОДНОСТЬ ДИСПЕРСИЙ. ВЫБОРКИ РАЗНОГО ОБЪЕМА - ВЛИЯЮТ НА РЕЗУЛЬТАТ

    Barlet_test = stats.bartlett(f, h, sh)
    print(Barlet_test) # BartlettResult(statistic=0.4640521043406442, pvalue=0.7929254656083131)
    # RESULT: У выборок наблюдается однородность дисперсий

    # ДИСПЕРСИОННЫЙ АНАЛИЗ. более 2 групп = критерий Фишера

    Fisher_test = stats.f_oneway(f, h, sh)
    print(Fisher_test) # F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698693)
    # RESULT: Pvalue < alpha - принимает альтернативную гипотезу - между выборками есть различия

    ### РЕЗУЛЬТАТ ТЕСТА ###
    # принимает альтернативную гипотезу - между средним ростом спортсменов есть различия



    # ПРОВЕРЯЕМ МЕЖДУ КАКИМИ ВЫБОРКАМИ ЕСТЬ РАЗЛИЧИЯ. Pos hoc test
    # проверсти на вводных выборках нельзя из-за разной длины.
    # можно попробовать уравнять, добавив среднее значение в первую выборку
    f_m = np.mean(f)
    h_m = np.mean(h)
    sh_m = np.mean(sh)
    print('mean f, h, sh:', f_m, h_m, sh_m) # mean f, h, sh: 179.125 178.66666666666666 172.72727272727272
    f_2 = np.array([173, 175, 180, 178, 177, 185, 183, 182, 179])
    h_2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
    sh_2 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172])
    all = list(f_2) + list(h_2) + list(sh_2)

    df = pd.DataFrame({"score": all,
                       "group": np.repeat(['f_2', 'h_2', 'sh_2'], repeats=9)})
    tukey_test = pairwise_tukeyhsd(df["score"], df["group"], alpha=0.05)
    print(tukey_test)
    # Multiple Comparison of Means - Tukey HSD, FWER=0.05
    # ====================================================
    # group1 group2 meandiff p-adj   lower   upper  reject
    # ----------------------------------------------------
    #    f_2    h_2  -0.4444 0.9774  -5.8948 5.0059  False
    #    f_2   sh_2  -5.3333 0.0559 -10.7837  0.117  False
    #    h_2   sh_2  -4.8889 0.0846 -10.3393 0.5615  False
    # ----------------------------------------------------
    #
    # Process finished with exit code 0

    # ВЫВОД - почти нет различий между ростом выборок футболистов и хоккеистов.


test1()
