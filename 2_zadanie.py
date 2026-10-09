import math


def cosinusnoe_rasstoyanie(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Нельзя посчитать: векторы разной длины (" + str(len(vector1)) + " и " + str(len(vector2)) + ")")
        return
    if len(vector1) == 0:
        print("Нельзя посчитать: векторы пустые")
        return

    skalyar = 0
    for i in range(len(vector1)):
        skalyar = skalyar + vector1[i] * vector2[i]

    summa_kvadratov1 = 0
    summa_kvadratov2 = 0
    for i in range(len(vector1)):
        summa_kvadratov1 = summa_kvadratov1 + vector1[i] ** 2
        summa_kvadratov2 = summa_kvadratov2 + vector2[i] ** 2

    dlina1 = summa_kvadratov1 ** 0.5
    dlina2 = summa_kvadratov2 ** 0.5

    if dlina1 == 0 or dlina2 == 0:
        print("Нельзя посчитать: один из векторов нулевой (все элементы равны 0)")
        return

    pohozhest = skalyar / (dlina1 * dlina2)
    rasstoyanie = 1 - pohozhest
    print("Косинусное расстояние: " + str(rasstoyanie))
    return rasstoyanie


a = [1, 2, 3]
b = [4, 5, 6]
cosinusnoe_rasstoyanie(a, b)

c = [1, 2]
d = [1, 2, 3]
cosinusnoe_rasstoyanie(c, d)

e = [0, 0, 0]
f = [1, 2, 3]
cosinusnoe_rasstoyanie(e, f)
