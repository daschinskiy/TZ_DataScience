from datetime import datetime


def raznica_dney(data1, data2):
    format_daty = "%Y-%m-%d"
    data1 = datetime.strptime(str(data1), "%Y-%m-%d")
    data2 = datetime.strptime(str(data2), "%Y-%m-%d")
    raznica = (data2 - data1).days
    if raznica < 0:
        print("Разница отрицательная, абсолютное значение: " + str(abs(raznica)))
    return raznica


otvet = raznica_dney("2024-01-10", "2024-01-25")
print(otvet)

otvet2 = raznica_dney("2024-05-20", "2024-05-01")
print(otvet2)
