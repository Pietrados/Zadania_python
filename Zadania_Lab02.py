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





