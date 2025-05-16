import tkinter as tk

okno = tk.Tk()
okno.title("Moje první GUI")
okno.geometry("300x200")

label = tk.Label(okno, text = "Ahoj světe", pady=30)
label.pack()

okno.mainloop()