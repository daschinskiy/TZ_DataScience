def raspredelenie_zaprosov(zaprosy):
    statistika = {}
    vsego = len(zaprosy)
    for zapros in zaprosy:
        slova = zapros.split()
        kolvo = len(slova)
        if kolvo in statistika:
            statistika[kolvo] = statistika[kolvo] + 1
        else:
            statistika[kolvo] = 1

    for kolvo in sorted(statistika):
        procent = round(statistika[kolvo] / vsego * 100)
        if kolvo == 1:
            slovo = "слово"
        elif kolvo == 2 or kolvo == 3 or kolvo == 4:
            slovo = "слова"
        else:
            slovo = "слов"
        print(str(kolvo) + " " + slovo + ": " + str(procent) + "%")
    return statistika


search_queries = ["watch new movies", "coffee near me", "how to find the determinant",
"python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex",
"bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",
"Statistics courses online from top universities"]

raspredelenie_zaprosov(search_queries)
