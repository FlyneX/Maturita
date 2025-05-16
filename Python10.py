import tkinter as tk 

okno = tk.Tk()
okno.geometry("300x300")
okno.title("Převod cm na inch")

label = tk.Label(okno, text = "Zadejte hodnotu v cm:")
label.pack()

entry = tk.Entry(okno)
entry.pack()

def prevod_jednotek():
    try:
        entry.get()
        cm = float(entry.get())
        nasobeni = 1 / 2.54
        inch = cm * nasobeni
        vysledek_label = tk.Label(okno, text = f"{inch} inch")
        vysledek_label.pack()
    except ValueError:
        chybovy_label = tk.Label(okno, text = "Zadejte platné číslo")
        chybovy_label.pack()

tlacitko = tk.Button(okno, text = "klikni pro převod", command = prevod_jednotek)
tlacitko.pack()

okno.mainloop()