#from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("hello, GUI")
window.geometry("400x200")

label = tk.Label(window, text="hello, GUI!")
label.pack()

window.mainloop()