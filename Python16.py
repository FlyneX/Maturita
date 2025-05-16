import tkinter as tk

okno = tk.Tk()
okno.title("Přepínání obrázků")
okno.geometry("500x500")

obrazek1 = tk.PhotoImage(file="kote.png")
obrazek2 = tk.PhotoImage(file="koet2.png")
                                                                                               
aktualni_obrazek = obrazek1
label_obrazek = tk.Label(okno, image=aktualni_obrazek)
label_obrazek.pack()

def prepnout_obrazek():
    global aktualni_obrazek
    if aktualni_obrazek == obrazek1:
        aktualni_obrazek = obrazek2
    else:
        aktualni_obrazek = obrazek1
    label_obrazek.config(image=aktualni_obrazek)

tlacitko = tk.Button(okno, text="Přepni obrázek", command=prepnout_obrazek)
tlacitko.pack()

okno.mainloop()