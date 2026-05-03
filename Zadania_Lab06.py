
# **Zadanie 1** Utwórz program kalkulator (dzielenie, pierwiastkowanie), wykonaj
#
# obsługę wyjatków. Korzystając z **assert** sprawdź poprawność działania twojego kodu.
# import math
# def dzielenie(a, b):
#     return a / b
#
# def pierwiastkowanie(a):
#     return math.sqrt(a)
#
# print("Testowanie funkcji...")
# assert dzielenie(10, 2) == 5.0, "Błąd testu: 10 / 2 powinno równać się 5.0"
# assert dzielenie(9, 3) == 3.0, "Błąd testu: 9 / 3 powinno równać się 3.0"
#
# assert pierwiastkowanie(16) == 4.0, "Błąd testu: pierwiastek z 16 to 4.0"
# assert pierwiastkowanie(25) == 5.0, "Błąd testu: pierwiastek z 25 to 5.0"
# print("Wszystkie testy 'assert' przeszły pomyślnie! Kod jest poprawny.\n")
#
# print("--- KALKULATOR W AKCJI ---")
#
# try:
#     x = 10
#     y = 0
#     print(f"Próbuję podzielić {x} przez {y}...")
#     wynik = dzielenie(x, y)
#     print(f"Wynik: {wynik}")
# except ZeroDivisionError:
#     print("Wyjątek! Pamiętaj cholero, nie dziel przez zero!")
# except Exception as e:
#     print(f"Nieoczekiwany błąd: {e}")
#
# print("-" * 20)
#
# try:
#     liczba = -9
#     print(f"Próbuję wyciągnąć pierwiastek z liczby {liczba}...")
#     wynik = pierwiastkowanie(liczba)
#     print(f"Wynik: {wynik}")
# except ValueError:
#     print("Wyjątek! W liczbach rzeczywistych nie ma pierwiastków z liczb ujemnych!")
# except Exception as e:
#     print(f"Nieoczekiwany błąd: {e}")
