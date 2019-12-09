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


# =================================================Entries=================================================
ent1_var = StringVar()
ent2_var = StringVar()
ent3_var = StringVar()

lbl1 = Label(frm1, text="Start:",  padx=10, bg="gray60", pady=10,  justify=LEFT)
lbl1.place(relx=0.2, rely=0.4, anchor=W)
ent1 = Entry(frm1, textvariable=ent1_var, bd=5)
ent1.place(relx=0.35, rely=0.4, relwidth=0.3, anchor=W)

btn01 = Button(frm1, text="Today", bd= 5)
btn01.place(relx=0.7, rely=0.4, relwidth=0.15, anchor=W)

lbl2 = Label(frm1, text="End:", bg="gray60",  padx=10, pady=10,  justify=LEFT)
lbl2.place(relx=0.2, rely=0.5, anchor=W)
ent2 = Entry(frm1, textvariable=ent2_var, bd=5)
ent2.place(relx=0.35, rely=0.5, relwidth=0.3, anchor=W)

btn02 = Button(frm1, text="Today", bd= 5)
btn02.place(relx=0.7, rely=0.5, relwidth=0.15, anchor=W)

lbl3 = Label(frm1, text="Result:", bg="gray60",  padx=10, pady=10,  justify=LEFT)
lbl3.place(relx=0.2, rely=0.6, anchor=W)
ent3 = Entry(frm1, textvariable=ent3_var, bd=5)
ent3.place(relx=0.35, rely=0.6, relwidth=0.3, anchor=W)

btn2 = Button(frm1, text="Reset", bd= 5)
btn2.place(relx=0.7, rely=0.6, relwidth=0.15, anchor=W)

root.mainloop()