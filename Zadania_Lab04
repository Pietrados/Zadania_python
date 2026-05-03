#Zadanie 1
# import random
# import operator
# lista_1 = list(range(1,101))
# lista_2 =[random.randint(1,500) for i in range(100)]
# wynik1 = map(operator.sub, lista_1, lista_2)
# wynik = list(wynik1)
# print("lISTA1", lista_1[:10])
# print("lISTA2", lista_2[:10])
# print("WYNIK",wynik[:10])
#Zadanie 2
# import random
# import operator
# lista = [random.randint(-10, 20) for i in range(10000)]
# wynik = filter(
#     lambda x: operator.lt(x, 3) and operator.eq(operator.mod(x, 2), 0),
#     lista
# )
# selekcja = list(wynik)
# print("Wygenerowano:", lista)
# print("Znalezione:",selekcja)
# print("Pierwsze 10 wynikow:", selekcja[:10])
#Zadanie 3
# import itertools
# liczby = []
# generator = itertools.count(100, 5)
# for i in range(50):
#     kolejna_liczba =next(generator)
#     liczby.append(kolejna_liczba)
# print("Wygenerowalo:", liczby)
# print("Lista liczb:")
# print(liczby)
#Zadanie 4
# import itertools
# def funcycle(n):
#     sekwencja = 'INFORMATYKA'
#     cykl = itertools.cycle(sekwencja)
#     wynik = []
#     for _ in range(n):
#         wynik.append(next(cykl))
#     print(f"Pobrano {n} elementów: {' '.join(wynik)}")
#
# print("Wywołanie dla n = 5:")
# funcycle(5)
# print("\nWywołanie dla n = 15:")
# funcycle(15)
# print("\nWywołanie dla n = 22:")
# funcycle(22)
#Zadanie 5
# import itertools
# lista1 = [1,2,3]
# lista2 = ['a','b','c']
# lista3 = [True,False]
# iloczyn = list(itertools.product(lista1, lista2, lista3)) #itertools oblicza uklad kartenzjanski
# for element in iloczyn:# wypisuje wyniki dla czytelnosci
#     print(element)
# #Zadanie 6
# from itertools import islice
# def podziel_na_stale_podgrupy(indeksy, n):
#     iterator_listy = iter(indeksy)
#     rozmiar_podgrupy = len(indeksy) // n
#     return [list(islice(iterator_listy, rozmiar_podgrupy)) for _ in range(n)]
# print("\nJednorazowy podział na stałe grupy:", podziel_na_stale_podgrupy)
#Zadanie 7
#Zadanie 8
# def generator_wielokrotnosci(n):
#     wartosc = 4
#     for _ in range(n):
#         yield wartosc
#         wartosc *= 2
# n = 3
# moj_generator = generator_wielokrotnosci(n)
# print(next(moj_generator))
# print(next(moj_generator))
# print(next(moj_generator))
#Zadanie 9
# import random
# def generator_losowych_parzystych(liczba_elementow=1000, maksimum=100000000):
#     for _ in range(liczba_elementow):
#         yield random.randrange(0, maksimum + 1, 2)
# moj_generator = generator_losowych_parzystych()
# print("Pierwsze 10 wylosowanych liczb parzystych:")
# for _ in range(10):
#     print(next(moj_generator))

