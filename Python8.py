import tkinter as tk

okno = tk.Tk()
okno.title("Moje prní GUI")
okno.geometry("200x200")

label = tk.Label(okno, text = "výtej")
label.pack()

def pozdrav():
    novy_label = tk.Label(okno, text = "Ahoj")
    novy_label.pack()

tlacitko = tk.Button(okno, text = "klikni", command = pozdrav)
tlacitko.pack()

okno.mainloop()