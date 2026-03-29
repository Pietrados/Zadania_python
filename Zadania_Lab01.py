#Zadania_Lab01
'''python.

[Zadania uczelniaLab01.py](https://github.com/user-attachments/files/26333423/Zadania.uczelniaLab01.py)# Zadania_python
[Uplo#Zadanie_1_Lab01
from operator import index

#imiona = ["Antek","Krzysiek","Gabrysia","Aneta","Jakub","Kacper","Monika","Marek","Grzesiek","Ludwik"]
#szukane = input("Podaj imie:")
#try:
   # index = imiona.index(szukane)
   # print("Imie", szukane, "znajduje sie na pozycji:",index)
#except ValueError:
 #   print("Imie", szukane, "nie znajduje sie na liscie")
#liczba = imiona.count(szukane)
#print("Imie", szukane, "wystepuje", liczba, "razy")
#nowe_imie = input("Podaj imie do dodania na koniec:")
#imiona.append(nowe_imie)
#print("Lista po dodaniu na koniec:", imiona)
#nowe_imie2 = input("Podaj imie do wstawienia na 3 miejsce:")
#imiona.insert(2,nowe_imie2)
#print("Lista po dodaniu na 3 miejsce:", imiona)
#imiona.sort()
#print("Lista po sortowaniu:", imiona)
#usuniety = imiona.pop()
#print("Usunieto:", usuniety)
#print("Lista po usunieciu ostatniego:", imiona)
#nowe_imiona = ["Bartosz","Leon", "Maja"]
#imiona.extend(nowe_imiona)
#print("Lista koncowa:", imiona)
#Zadanie_2_Lab01
# slownik = {
#     "imie":["Kacper", "Sebastian", "Bartek"],
#     "nazwisko":["Pietraszkiewicz","Kowal","Nowak"],
#     "wiek":[19, 22, 45]
# }
# numer = int(input("Podaj numer osoby od 1 do 3:"))
# indeks = numer - 1
# print("Imie:",     slownik ["imie"][indeks])
# print("Nazwisko:", slownik ["nazwisko"][indeks])
# print("Wiek:",     slownik["wiek"][indeks])
# #Zadanie_3_Lab01
# kierunek = input("\nPodaj kierunek studiow dla tej osoby:")
# slownik['kierunek_studiow'] = ['','','']
# slownik['kierunek_studiow'][indeks] = kierunek
# print("\nZaktualizowane dane osoby nr:",numer)
# print("Imie:", slownik ["imie"][indeks])
# print("Nazwisko:", slownik ["wiek"][indeks])
# print("Wiek:", slownik["wiek"][indeks])
# print("Kierunek studiow:", slownik["kierunek_studiow"][indeks])
# print("\nAktualny slownik:",slownik)
#Zadanie_4_Lab01
# for klucz, wartosc in slownik.items():
#     print("klucz:", klucz, "--> liczba elementow:",len(wartosc))
#Dodatkowe zadania z listy Lab_01
# print(0>1)
# print(0<=1)
# print(0>=1)
# print(1==0)
# print(1==1)
# print(1 != 0)
# print(1 !=1)

# x =int(input("Podaj jakis x:"))
# y = int(input("Podaj jakis y:"))
# suma = 2*x+5*y
# print("Wynik to:",suma)

# a = input("Podaj imie:")
# b = input("Podaj Nazwisko:")
# c = int(input("Podaj wiek:"))
# d = input("Podaj kierunek studiow:")
# print("Jestem",a,b, "mam",c,"lat studiuje",d)

#print(1+2+10+20000001+4+347586970885 == 321784560456434534646)

# a = int(input("Podaj pierwsza liczbe:"))
# b = int(input("Podaj druga liczbe:"))
# suma = a + b
# if suma % 2 == 0:
#     print("Liczba jest parzysta", suma)
# else:
#     print("Liczba jest nieparzysta", suma )

# a = int(input("Podaj pierwsza liczbe:"))
# b = int(input("Podaj druga liczbe:"))
# suma = a + b
# print("Suma twoich liczb to:", suma)
# roznica = a - b
# print("Roznica twoich liczb to:", roznica)
# iloczyn = a * b
# print("Iloczyn twoich liczb to:", iloczyn)
# iloraz = a / b
# print("Iloraz twoich liczb to:", iloraz)
# potega = a**b
# print("Potega twoich liczb to:", potega)

# x = int(input("Podaj liczbę x: "))
#
# wynik1 = (x > 1 and x < 13)   # x musi być jednocześnie >1 i <13
# wynik2 = (x != 5 or x < 0)    # wystarczy że x różne od 5 LUB ujemne
#
# print(f"x = {x}")
# print(f"(x > 1 and x < 13) = {wynik1}")
# print(f"(x != 5 or x < 0)  = {wynik2}")

# print("---To jest mini ankieta, prosze odpowiedz mi na te pytania---")
# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# wiek = input("Podaj wiek: ")
# odzywianie = input("Czy zdrowo sie odzywiasz?:")
# if odzywianie.lower() == "tak":
#     print("Super oby tak dalej")
# elif odzywianie.lower() == "nie":
#     print("Musisz nad tym popracowac")
# else:
#     print("Nie rozumiem odpowiedzi, wpisz tak lub nie")
#
# sport = input("Czy lubisz sport?:")
# if sport.lower() == "tak":
#     print (input("O super, a uprawiasz jakis:?"))
#     print("Wow to mega fajnie")
# elif sport.lower() == "nie":
#     print("Aj szkoda")
# else:
#     print("Nie rozumiem odpowiedzi, wpisz tak lub nie")












ading Zadania uczelniaLab01.py…]()
