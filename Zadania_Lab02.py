#Zadanie 1
# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                  'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
#
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                  'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
#
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC11',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                  'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
#
# # a) Wspólne dla wszystkich 3 pacjentów
# all_common = set_gene1 & set_gene2 & set_gene3
#
# # b) Wspólne dla dokładnie 2 pacjentów
# only_p1_p2 = (set_gene1 & set_gene2) - set_gene3
# only_p1_p3 = (set_gene1 & set_gene3) - set_gene2
# only_p2_p3 = (set_gene2 & set_gene3) - set_gene1
#
# # c) Wyłącznie u jednego pacjenta
# only_p1 = set_gene1 - set_gene2 - set_gene3
# only_p2 = set_gene2 - set_gene1 - set_gene3
# only_p3 = set_gene3 - set_gene1 - set_gene2
#
# # Wyniki
# print("=" * 55)
# print("a) Wspólne dla WSZYSTKICH 3 pacjentów:")
# print(f"   {sorted(all_common)}\n")
#
# print("=" * 55)
# print("b) Wspólne dla dokładnie 2 pacjentów:")
# print(f"   Pacjent 1 & 2: {sorted(only_p1_p2)}")
# print(f"   Pacjent 1 & 3: {sorted(only_p1_p3)}")
# print(f"   Pacjent 2 & 3: {sorted(only_p2_p3)}\n")
#
# print("=" * 55)
# print("c) Wyłącznie u jednego pacjenta:")
# print(f"   Tylko Pacjent 1: {sorted(only_p1)}")
# print(f"   Tylko Pacjent 2: {sorted(only_p2)}")
# print(f"   Tylko Pacjent 3: {sorted(only_p3)}")
# print("=" * 55)
# Zadanie 2
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3', 'GALNT14', 'ERCC1',
#                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
#
# geny_do_znalezienia = ['FGFR4', 'FGERA4']
#
# print("=" * 45)
# for gen in geny_do_znalezienia:
#     indeksy = [i for i, g in enumerate(lista_gene1) if g == gen]
#     if indeksy:
#         print(f"Gen '{gen}' ZNALEZIONY — indeks/y: {indeksy}")
#     else:
#         print(f"Gen '{gen}' NIE ZNALEZIONY na liście")
# print("=" * 45)
#Zadanie 3
# word = 'Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza.'
# print("="*55)
# liczba_Emma = word.count('Emma')
# print("Liczba wystapien Emma:", liczba_Emma)
# word_duze = word.upper()
# print("Tekst duzymi literami:")
# print(word_duze)
# print("="*55)
# lista_wyrazow = word.split()
# print("="*55)
# print(lista_wyrazow)
# print("Laczna liczba wyrazow:", lista_wyrazow)
#Zadanie 4
# x = int (input("Podaj liczbe x:"))
# if x % 2 == 0:
#     print("Liczba parzysta")
# else:
#     x % 2 != 0
#     print("Liczba nieparzysta")
#Zadanie 5
# punkty = float(input("Podaj liczbe uzyskanych punktow (max 15):"))
# if punkty < 0 or punkty > 15:
#     print("Blad! Punkty musza byc w zakresie od 0 do 15")
# else:
#     procent = (punkty / 15) * 100
#     match True:
#         case _ if procent >= 91:
#             ocena =  5.0
#         case _ if procent >= 81:
#                 ocena = 4.5
#         case _ if procent >= 71:
#             ocena = 4.0
#         case _ if procent >= 61:
#             ocena = 3.5
#         case _ if procent >= 51:
#             ocena = 3.0
#         case _:
#             ocena = 2.0
#     print("Uzyskane punkty:", punkty)
#     print("Uzyskany procent:", procent)
#     print("Uzyskana ocena:",ocena)

#Zadanie 6
# n = int(input("Podaj liczbe n:"))
# suma = 0
# for i in range (1, n + 1):
#     suma = suma + (1 / i)
# print("Suma dla n =", n, "wynosi", suma)
#Zadanie 7
# liczba = 1
# while liczba <= 10:
#     pierwiastek = liczba**0.5
#     print("Pierwiastek z", liczba, "wynosi", round(pierwiastek, 2))
#     liczba = liczba + 1
#Zadanie 8
# import math
# a = float(input("Podaj liczbe a:"))
# b = float(input("Podaj liczbe b:"))
# c = float(input("Podaj liczbe c:"))
# if a == 0:
#     print("a nie moze byc zerem!")
# else:
#     delta = b**2 - 4*a*c
#     print("Delta wynosi:", delta)
#     if delta > 0:
#         pierwiastek_z_delty = math.sqrt(delta)
#         x1 = (-b + math.sqrt(delta))/(2*a)
#         x2 = (-b - math.sqrt(delta))/(2*a)
#         print("x1 =" ,round(x1))
#         print("x2 =" ,round(x2))
#     elif delta == 0:
#         x0 = -b/(2*a)
#         print("x0 =" , x0)
#     elif delta < 0:
#         print("Delta jest ujemna, wiec nie ma rozwiazan")
#Zadanie 9
# for liczba in range(1,1001):
#     if liczba % 2 == 0:
#         print(liczba, end=' ')
#Zadanie 10
# while True:
#     dane1 = input("Podaj pierwsza liczbe: ")
#     if dane1 == "0":
#         print("Wpisanie '0' skutkuje zakonczeniem programu")
#         break
#     dane2 = input("Podaj druga liczbe: ")
#     if dane2 == "0":
#         print("Wpisanie '0' skutkuje zakonczeniem programu")
#         break
#     try:
#         liczba1 = int(dane1)
#         liczba2 = int(dane2)
#         iloczyn = liczba1 * liczba2
#         print("Iloczyn liczb to:", iloczyn)
#     except ValueError:
#         print("Blad, iloraz mozna wykonac tylko na liczbach calkowitych")
#Zadanie 11
# print('-'*35)
# print("Uzytkownik: Kacper Pietraszkiewicz")
# print('-'*35)
# poprawne_hasla = ("haslo1234", "tajnehaslo")
# wpisane_haslo = input("Podaj haslo:")
# if wpisane_haslo in poprawne_hasla:
#     print("Haslo jest poprawne")
# else:
#     print("Haslo nie jest poprawne, sprobuj ponwonie")
#Zadanie 12
# import random
# moje_liczby = (random.sample(range(0, 100), 100))
# print("Bez posortowania:", moje_liczby)
# posortowane = sorted(moje_liczby)
# print("Posortowane:", posortowane)
#Zadanie 13
# print('-'*35)
# print("Uzytkownik: Kacper Pietraszkiewicz")
# print('-'*35)
# poprawne_hasla = ("haslo1234", "tajnehaslo")
# while True:
#     wpisane_haslo = input("Podaj haslo:")
#     if wpisane_haslo in poprawne_hasla:
#         print("Haslo jest poprawne")
#         break
#     else:
#         print("Haslo nie jest poprawne, sprobuj ponwonie")
#Zadanie 14
# iloraz = lambda a, b, c: a / b / c
# print(iloraz(36, 6, 6))





