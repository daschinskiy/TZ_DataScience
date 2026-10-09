def chotnie_bez_dublikatov(spisok):
    spisok = list(spisok)
    chotnie = []
    for chislo in spisok:
        if chislo % 2 == 0:
            if chislo not in chotnie:
                chotnie.append(chislo)
    result = sorted(chotnie)
    result.reverse()
    return result


moi_chisla = [1, 2, 3, 4, 4, 6, 8, 2, 10, 7, 10, 5]
otvet = chotnie_bez_dublikatov(moi_chisla)
print(otvet)
