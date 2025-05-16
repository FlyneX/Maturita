import tkinter as tk 

okno = tk.Tk()
okno.geometry("300x300")

entry = tk.Entry(okno)
entry.pack()

def entry_get():
    label = tk.Label(okno, text = entry.get())
    label.pack()

tlacitko = tk.Button(okno, text = "odeslat", command = entry_get)
tlacitko.pack()

okno.mainloop()
