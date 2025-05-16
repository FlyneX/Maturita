import tkinter as tk 

okno = tk.Tk()
okno.geometry("300x300")
okno.title("PŘEVEĎ TEPLOTU")

volba = tk.StringVar()
volba.set("F_na_C")

rb1 = tk.Radiobutton(okno, text = "°F na °C", variable=volba, value="F_na_C")
rb1.pack()

rb2 = tk.Radiobutton(okno, text = "°C na °F", variable=volba, value="C_na_F")
rb2.pack()

entry = tk.Entry(okno)
entry.pack()

vysledek_label = tk.Label(okno, text="")

def preved():
    try:
        hodnota = float(entry.get())

        if volba.get() == "F_na_C":
            vysledek = 5/9 * (hodnota - 32)
            jednotka = "°C"

        else:
            vysledek = (hodnota / (5/9)) + 32
            jednotka = "°F"

        if (volba.get() == "F_na_C" and vysledek < 10) or (volba.get() == "C_na_F" and vysledek < 50):
            barva = "blue"

        elif (volba.get() == "F_na_C" and vysledek > 25) or (volba.get() == "C_na_F" and vysledek > 77):
            barva = "red"

        else:
            barva = "green"

        vysledek_label.config(text=f"Výsledek: {round(vysledek, 2)} {jednotka}", fg = barva)

    except ValueError:
        vysledek_label.config(text="Zadejte platné číslo!")

tlacitko = tk.Button(okno, text="Převeď", command=preved)
tlacitko.pack()

vysledek_label.pack()

okno.mainloop()