import tkinter as tk

okno = tk.Tk()
okno.geometry("600x400")
okno.title("Můj první formulář")

# přidání textu (label)
label = tk.Label(okno, text="Zadej své jméno:")
label.pack()

# vstupní pole (entry)
vstup = tk.Entry(okno)
vstup.pack()

# tlačítko
def klik():
    print("Zadal jsi:", vstup.get())

tlacitko = tk.Button(okno, text="Potvrdit", command=klik)
tlacitko.pack()

okno.mainloop()