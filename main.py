from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time


root = Tk()
root.title("Eventer")
root.iconbitmap("Photo\\calendar.ico")
root.minsize(600, 500)

frm = Frame(root, bg="gray20")
frm.place(relx=0, rely=0, relwidth=1, relheight=1)

frm1 = Frame(frm, bg="gray60")
frm1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

title = Label(frm1, text="Date Calculator", font=20, bg="gray60", padx=10, pady=10)
title.place(relx=0.5, rely=0.2, anchor=N)

root.mainloop()