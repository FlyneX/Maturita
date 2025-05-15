import tkinter as tk

okno = tk.Tk()
okno.geometry("600x400")
okno.title("Vitasmrdi")


lbl = tk.Label(okno, text="je tomu tak", bg="aqua", font=10)
lbl.pack()

okno.mainloop()