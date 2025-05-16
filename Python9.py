import tkinter as tk

okno = tk.Tk()
okno.title("GUI")
okno.geometry("300x300")

label = tk.Label(okno, text = "zadejte své jméno")
label.pack()

entry = tk.Entry(okno)
entry.pack()

def zapsani_jmena():
    jmeno = entry.get()
    vysledek = tk.Label(okno, text = "")
    vysledek.pack()
    vysledek.config(text = f"Ahoj, {jmeno}")

tlacitko = tk.Button(okno, text = "klikni pro pozdrav", command = zapsani_jmena)
tlacitko.pack()



okno.mainloop()