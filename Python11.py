import tkinter as tk 

okno = tk.Tk()
okno.geometry("300x300")
okno.title("PŘEVEĎ JEDNOTKU, BABY")

volba = tk.StringVar()
volba.set("cm_to_inch")

rb1 = tk.Radiobutton(okno, text = "cm to inch", variable=volba, value="cm_to_inch")
rb1.pack()

rb2 = tk.Radiobutton(okno, text = "inch to cm", variable=volba, value="inch_to_cm")
rb2.pack()

def zobrazit_volbu():
    label = tk.Label(okno, text = f"vybrana volba je: {volba.get()}")
    label.pack()

entry = tk.Entry(okno)
entry.pack()

def preved():
    try:
        hodnota = float(entry.get())

        if volba.get() == "cm_to_inch":
            vysledek = hodnota / 2.54
            jednotka = "inch"
        else:
            vysledek = hodnota * 2.54
            jednotka = "cm"

        label = tk.Label(okno, text=f"Výsledek: {round(vysledek, 2)} {jednotka}")
        label.pack()

    except ValueError:
        chyba = tk.Label(okno, text="Zadejte platné číslo!")
        chyba.pack()

tlacitko = tk.Button(okno, text = "zobrazit volbu", command=zobrazit_volbu)
tlacitko.pack()

tlacitko = tk.Button(okno, text="Převeď", command=preved)
tlacitko.pack()

okno.mainloop()