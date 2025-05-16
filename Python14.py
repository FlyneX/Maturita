import tkinter as tk 

okno = tk.Tk()
okno.title("barva")
okno.geometry("300x300")

label = tk.Label(okno, text = "Ahoj")

def zmena_pozdravu():
    if label.cget("text") == "Ahoj":
        label.config(text = "Čau")
    else:
        label.config(text = "Ahoj")

label.pack()

tlacitko2 = tk.Button(okno, text = "Změň pozdrav", command = zmena_pozdravu)
tlacitko2.pack()

volba = tk.StringVar()
volba.set("green")

rb1 = tk.Radiobutton(okno, text = "Zelená", variable=volba, value="green")
rb1.pack()

rb2 = tk.Radiobutton(okno, text = "Červená", variable=volba, value="red")
rb2.pack()

rb3 = tk.Radiobutton(okno, text = "Modrá", variable=volba, value="blue")
rb3.pack()

def zmena_pozadi():
    if volba.get() == "green":
        okno.config(bg="green")
    elif volba.get() == "red":
        okno.config(bg = "red")
    else:
        okno.config(bg = "blue")

tlacitko = tk.Button(okno, text = "Změň barvu", command = zmena_pozadi)
tlacitko.pack()

okno.mainloop()