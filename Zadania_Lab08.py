#from tkinter import *
# window = Tk()
# window.title("ty")
# window.geometry("400x400")
# def callback():  # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#       try:
#           if var.get() == 1:
#             result = int(entry1.get()) + int(entry2.get())
#           if var.get() == 2:
#             result = int(entry1.get()) - int(entry2.get())
#       except ValueError as e:
#           showerror("Box:", e)
#
#       txt = "Result: " + str(result)
#       text3.config(text=txt)  # ustawienie tekstu w kontrolce o nazwie etykieta_text3
# window.mainloop()
# def callfun3():
#   filewin = Toplevel(window)
#   button = Button(filewin, text="W trakcie roboty")
#   button.pack()
#
# window = Tk()
# menubar = Menu(window)
# my_menu = Menu(menubar, tearoff=0)
#
# my_menu.add_command(label="New", command=callfun3)
# my_menu.add_command(label="Open", command=callfun3)
# my_menu.add_command(label="Save", command=callfun3)
# my_menu.add_separator()
# my_menu.add_command(label="Exit", command=window.quit)
#
# menubar.add_cascade(label="File", menu=my_menu)
# window.config(menu=menubar)
# window.mainloop()
# def callfun1():
#   result = var1.get() + var2.get() + var3.get()
#   my_text = "A + B + C= " + str(result)
#   text3.config(text=my_text)
#
# window = Tk()
# window.geometry("150x400")
#
# Label(window, text="A", bg="green", fg="white").grid(row=1, column=1)
#
# var1 = IntVar()
# Scale(window, from_=0, to=100, variable=var1).grid(row=2, column=1)
#
# Label(window, text="B", bg="red", fg="white").grid(row=3, column=1)
#
# var2 = IntVar()
# Scale(window, from_=0, to=50, orient=HORIZONTAL, variable=var2).grid(row=4, column=1)
#
# Button(window, text="A + B + C", command=callfun1, fg="red").grid(row=8, column=1)
#
# Label(window, text="C", bg="blue", fg="white").grid(row=5, column=1)
# var3 = IntVar()
#
# Scale(window, from_=0, to=75, variable=var3).grid(row=6, column=1)
#
#
#
# text3 = Label(window, text=" ")
# text3.grid(row=9, column=1)
#
# window.mainloop()
# def callfun2():
#   if var1.get() == 1 and var2.get() == 0:
#     text.config(text="I like to receive gifts")
#
#   if var1.get() == 0 and var2.get() == 1:
#     text.config(text="I like to give gifts")
#
#   if var1.get() == 1 and var2.get() == 1:
#     text.config(text="I like to receive/give gifts")
#
# window = Tk()
# window.geometry("400x400")
#
# var1 = IntVar()
# Checkbutton(window,
#             text="I like to receive gifts",
#             variable=var1,
#             command=callfun2).grid(row=0, sticky=W)
# #  the sticky option specifies which side the widget should stick to and how to distribute any extra space within the cell that is not taken up by the widget at its original size.
# # sticky = W - left-align (wyrównaj do lewej)
#
# # Setting default value of a checkbutton
#  #
#
# var2 = IntVar()
# Checkbutton(window,
#             text="I like to give gifts",
#             variable=var2,
#             command=callfun2).grid(row=1, sticky=W)
# var2.set(1)
# text = Label(window, text="Result: ")
# text.grid(row=4, column=1)
#
# window.mainloop()
# Zadanie 1
# # Kalkulator: utwórz 2 kontrolki typu edit tekst, 1 przycisk "ok" i radiobutton
# # po wcisnieciu przycisku program powinien wykonywać 4 dowolne operacje matematyczne na liczbach wpisanych przez użytkownika
# # w kontrolkach edit
# # Obsłuż potencjalne błędy wpisując własny komentarz: np. TypeError
# # Do wyswietlania komunikatów użyj okienek komunikacyjnych
import tkinter as tk
from tkinter import messagebox


def wykonaj_obliczenia():
    try:

        liczba1_str = pole_tekstowe1.get()
        liczba2_str = pole_tekstowe2.get()

        liczba1 = float(liczba1_str)
        liczba2 = float(liczba2_str)

        operacja = wybor_operacji.get()


        if operacja == 1:
            wynik = liczba1 + liczba2
            nazwa = "Dodawanie"
        elif operacja == 2:
            wynik = liczba1 - liczba2
            nazwa = "Odejmowanie"
        elif operacja == 3:
            wynik = liczba1 * liczba2
            nazwa = "Mnożenie"
        elif operacja == 4:
            if liczba2 == 0:

                raise ZeroDivisionError("Nie mozna przez '0'")
            wynik = liczba1 / liczba2
            nazwa = "Dzielenie"
        else:
            raise ValueError("Nie wybrano operacji.")
        messagebox.showinfo("Wynik", f"Wynik operacji ({nazwa}):\n{wynik}")

    except ValueError:
        messagebox.showerror(" Blad: TypeError / ValueError",
                             "Wprowadzono nieprawidlowe dane! Upewnij się, że wpisujesz tylko liczby.")
    except ZeroDivisionError as e:
        messagebox.showwarning("Blad matematyczny", str(e))
    except Exception as e:
        messagebox.showerror("Blad", f"Wystapil nieoczekiwany blad:\n{e}")


okno = tk.Tk()
okno.title("Kalkulator - Zadanie 1")
okno.geometry("300x350")


tk.Label(okno, text="Pierwsza liczba x:").pack(pady=(10, 0))
pole_tekstowe1 = tk.Entry(okno)
pole_tekstowe1.pack()

tk.Label(okno, text="Druga liczba y:").pack(pady=(10, 0))
pole_tekstowe2 = tk.Entry(okno)
pole_tekstowe2.pack()

wybor_operacji = tk.IntVar()
wybor_operacji.set(1)

tk.Label(okno, text="Wybierz operacje:").pack(pady=(15, 5))
tk.Radiobutton(okno, text="Dodawanie (+)", variable=wybor_operacji, value=1).pack()
tk.Radiobutton(okno, text="Odejmowanie (-)", variable=wybor_operacji, value=2).pack()
tk.Radiobutton(okno, text="Mnozenie (*)", variable=wybor_operacji, value=3).pack()
tk.Radiobutton(okno, text="Dzielenie (/)", variable=wybor_operacji, value=4).pack()

przycisk_ok = tk.Button(okno, text="OK", width=10, command=wykonaj_obliczenia)
przycisk_ok.pack(pady=20)

okno.mainloop()
