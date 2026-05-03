#Zadania a
# def poteguj_kaskadowo(*args):
#     if len(args) > 100:
#         return "Blad: Zbyt wiele parametrów wejściowych (maksymalnie 100)."
#     return tuple(x ** x for x in args)
#
#
# def uruchom_program():
#     dane_wejsciowe = input("Wprowadź liczby calkowite rozdzielone przecinakmi : ")
#
#     try:
#         liczby = [int(x.strip()) for x in dane_wejsciowe.split(',') if x.strip()]
#         if not liczby:
#             print("Nie liczb.")
#             return
#         wynik = poteguj_kaskadowo(*liczby)
#
#         print("\nWyniki obliczeń:")
#         print(wynik)
#
#     except ValueError:
#         print("Blad:Wpisz(np. 2, 3, 4).")
# if __name__ == "__main__":
#     uruchom_program()
# def uruchom_dynamiczny_kalkulator():
#     dane_wejsciowe = input("Wprowadź ciąg liczb rozdzielonych przecinkami (np. 2, 3, 4): ")
#
#     try:
#         liczby = [int(x.strip()) for x in dane_wejsciowe.split(',') if x.strip()]
#     except ValueError:
#         print("Błąd: Wszystkie wprowadzone wartości muszą być prawidłowymi liczbami całkowitymi.")
#         return
#
#     n = len(liczby)
#
#     if n > 100:
#         print("Błąd: Liczba parametrów wejściowych jest większa niż 100.")
#         return
#     if n == 0:
#         print("Błąd: Nie podano żadnych liczb.")
#         return
#     args_str = ", ".join([f"x{i + 1}" for i in range(n)])
#     return_str = ", ".join([f"x{i + 1}**x{i + 1}" for i in range(n)])
#     docstring_args = "\n".join([f"        x{i + 1} (int): Dynamiczny parametr {i + 1}." for i in range(n)])
#
#     func_code = f'''
# def dynamiczna_funkcja_potegujaca({args_str}):
#     """
#     Oblicza potęgę (x^x) dla każdego dynamicznie nazwanego parametru.
#
#     Args:
# {docstring_args}
#
#     Returns:
#         {"int" if n == 1 else "tuple"}: Obliczone wartości potęg.
#     """
#     return {return_str}
# '''
#     local_env = {}
#     exec(func_code, globals(), local_env)
#     dynamiczna_funkcja = local_env['dynamiczna_funkcja_potegujaca']
#     wynik = dynamiczna_funkcja(*liczby)
#
#
#     print("\n--- Wynik działania ---")
#     print(f"Dynamicznie wygenerowana sygnatura: def dynamiczna_funkcja_potegujaca({args_str})")
#     print(f"Wynik: {wynik}")
#
# if __name__ == "__main__":
#     uruchom_dynamiczny_kalkulator()
#Zadania b
#Zadanie 1
# import os
# def zmien_i_wyswietl_katalog(sciezka):
#
#     try:
#         os.chdir(sciezka)
#         obecny_katalog = os.getcwd()
#         print(f"Pomyślnie zmieniono katalog na:\n> {obecny_katalog}\n")
#         zawartosc = os.listdir(obecny_katalog)
#
#         print("Zawartość katalogu:")
#         if not zawartosc:
#             print(" (Katalog jest pusty)")
#         else:
#             for element in zawartosc:
#                 print(f" - {element}")
#
#     except FileNotFoundError:
#         print(f"Błąd: Katalog o podanej ścieżce '{sciezka}' nie istnieje.")
#     except NotADirectoryError:
#         print(f"Błąd: Podana ścieżka '{sciezka}' wskazuje na plik, a nie na katalog.")
#     except PermissionError:
#         print(f"Błąd: Brak uprawnień do odczytu lub wejścia do katalogu '{sciezka}'.")
#     except Exception as e:
#         print(f"Wystąpił nieoczekiwany błąd: {e}")
#
# sciezka_uzytkownika = input("Podaj sciezke do katalogu: ")
# zmien_i_wyswietl_katalog(sciezka_uzytkownika)
#Zadanie 2
# import os
# def zmien_i_wyswietl_katalog(sciezka):
#
#     try:
#         os.chdir(sciezka)
#         obecny_katalog = os.getcwd()
#         print(f"\n[SUKCES] Zmieniono katalog na: {obecny_katalog}\n")
#         zawartosc = os.listdir(obecny_katalog)
#         print("Zawartość katalogu:")
#         if not zawartosc:
#             print(" (Katalog jest pusty)")
#         else:
#             for element in zawartosc:
#                 print(f" - {element}")
#     except FileNotFoundError:
#         print(f"Błąd: Katalog '{sciezka}' nie istnieje.")
#     except NotADirectoryError:
#         print(f"Błąd: Ścieżka '{sciezka}' wskazuje na plik.")
#     except PermissionError:
#         print(f"Błąd: Brak uprawnień do katalogu '{sciezka}'.")
#     except Exception as e:
#         print(f"Wystąpił nieoczekiwany błąd: {e}")
# def testuj_zmiane_katalogu():
#     print("--- Uruchomienie programu ---")
#
#     while True:
#
#         odpowiedz = input('Czy mam zmienić katalog? ').strip().lower()
#
#         if odpowiedz == "yes":
#
#             print("\nŚwietnie! Przechodzimy dalej.")
#             sciezka_uzytkownika = input("Podaj ścieżkę do nowego katalogu: ")
#
#             zmien_i_wyswietl_katalog(sciezka_uzytkownika)
#             break
#         else:
#             print('Błąd: Program działa tylko po wpisaniu "yes". Spróbuj ponownie!\n')
# if __name__ == "__main__":
#     testuj_zmiane_katalogu()
#Zadanie 3
# import os
# if not os.path.exists("Dokument"):
#     os.mkdir("Dokument")
# os.chdir("Dokument")
#
#
# open("Lab1.doc", "w").close()
# open("Lab2.doc", "w").close()
# open("Lab3.doc", "w").close()
#
# open("Notatki.txt", "w").close()
# print("--- ZADANIE A ---")
# wszystkie_pliki = os.listdir()
# print("Wszystkie pliki w folderze roboczym:")
# print(wszystkie_pliki)
# print("\n--- ZADANIE B ---")
# print("Tylko pliki z rozszerzeniem .doc:")
# for plik in wszystkie_pliki:
#     if plik.endswith(".doc"):
#         print(plik)
#Zadanie 4
# import os
#
# os.makedirs("StudentDoc", exist_ok=True)
# os.makedirs("StudentObrazy", exist_ok=True)
#
#
# with open(os.path.join("StudentDoc", "notatka1.txt"), "w", encoding="utf-8") as plik:
#     plik.write("To jest krótka notatka numer 1.")
#
# with open(os.path.join("StudentDoc", "wyklad2.txt"), "w", encoding="utf-8") as plik:
#     plik.write("To jest znacznie dłuższy tekst z wykładu numer 2, aby rozmiar pliku był nieco większy.")
# with open(os.path.join("StudentObrazy", "wykres.jpg"), "wb") as plik:
#     plik.write(b'\x00' * 1024)
#
# with open(os.path.join("StudentObrazy", "logo_uczelni.png"), "wb") as plik:
#     plik.write(b'\x00' * 2048)  # Tu wpisujemy 2048 bajtów (2 KB)
#
#
#
# def wyswietl_info_o_katalogu(nazwa_katalogu):
#     print(f"\nZawartość folderu '{nazwa_katalogu}':")
#
#     pliki = os.listdir(nazwa_katalogu)
#
#     if not pliki:
#         print(" - Katalog jest pusty")
#     else:
#         for nazwa_pliku in pliki:
#
#             pelna_sciezka = os.path.join(nazwa_katalogu, nazwa_pliku)
#
#             rozmiar = os.path.getsize(pelna_sciezka)
#             print(f" - {nazwa_pliku} (Rozmiar: {rozmiar} bajtów)")
#
# wyswietl_info_o_katalogu("StudentDoc")
# wyswietl_info_o_katalogu("StudentObrazy")
# #Zadanie 5
# import os
#
#
# stara_nazwa = "KatalogPoczatkowy"
# nowa_nazwa = "ZmienionyKatalog"
#
#
# if not os.path.exists(stara_nazwa):
#     os.mkdir(stara_nazwa)
#     print(f"Krok 1: Pomyślnie utworzono katalog o nazwie '{stara_nazwa}'.")
# else:
#     print(f"Krok 1: Katalog '{stara_nazwa}' już istnieje.")
#
#
# if os.path.exists(stara_nazwa) and not os.path.exists(nowa_nazwa):
#     os.rename(stara_nazwa, nowa_nazwa)
#     print(f"Krok 2: Pomyślnie zmieniono nazwę z '{stara_nazwa}' na '{nowa_nazwa}'.")
# else:
#     print(f"Krok 2: Nie można zmienić nazwy. Sprawdź, czy '{nowa_nazwa}' już nie istnieje.")
#
# print("\nObecne elementy w folderze roboczym:")
# for element in os.listdir():
#     if element == nowa_nazwa:
#         print(f" -> {element} (Nasz folder!)")
# #Zadanie 6
# import pickle
# import os
#
#
# nazwa_pliku = "moje_listy.pkl"
#
#
# lista1 = [1, 2, 3, 4, 5]
# lista2 = ["jabłko", "banan", "czereśnia"]
# lista3 = [True, False, 3.14, "tekst"]
#
# print("--- Etap 1: Utworzenie list ---")
# print("Lista 1:", lista1)
# print("Lista 2:", lista2)
# print("Lista 3:", lista3)
#
# with open(nazwa_pliku, "wb") as plik_zapisu:
#
#     pickle.dump(lista1, plik_zapisu)
#     pickle.dump(lista2, plik_zapisu)
#     pickle.dump(lista3, plik_zapisu)
#
# print(f"\n--- Etap 2: Zapisano wszystkie listy do pliku '{nazwa_pliku}' ---")
#
# del lista1
# del lista2
# del lista3
#
# print("\n--- Etap 3: Usunięto listy z pamięci RAM ---")
#
# print("\n--- Etap 4: Odczytywanie danych z pliku ---")
#
# if os.path.exists(nazwa_pliku):
#     with open(nazwa_pliku, "rb") as plik_odczytu:
#
#         odczytana_lista1 = pickle.load(plik_odczytu)
#         odczytana_lista2 = pickle.load(plik_odczytu)
#         odczytana_lista3 = pickle.load(plik_odczytu)
#
#     print("Odczytana Lista 1:", odczytana_lista1)
#     print("Odczytana Lista 2:", odczytana_lista2)
#     print("Odczytana Lista 3:", odczytana_lista3)
# else:
#     print(f"Błąd: Nie znaleziono pliku '{nazwa_pliku}'.")
