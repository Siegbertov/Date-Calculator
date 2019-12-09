from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time


def set_today1():
    cur = time.strftime("%d/%m/%Y")
    ent1.insert(END, cur)

def set_today2():
    cur = time.strftime("%d/%m/%Y")
    ent2.insert(END, cur)

def reset_main():
    ent1_var.set("")
    ent2_var.set("")
    ent3_var.set("")

def eval_date():
    d1 = ent1.get()
    d2 = ent2.get()
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")
    ent3_var.set(abs((d2-d1).days))

def exit_main():
    QExit = messagebox.askyesno("Eventer", "Confirm if you want to exit")
    if QExit:
        root.destroy()
    else:
        pass

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

btn01 = Button(frm1, text="Today", bd= 5, command=set_today1)
btn01.place(relx=0.7, rely=0.4, relwidth=0.15, anchor=W)

lbl2 = Label(frm1, text="End:", bg="gray60",  padx=10, pady=10,  justify=LEFT)
lbl2.place(relx=0.2, rely=0.5, anchor=W)
ent2 = Entry(frm1, textvariable=ent2_var, bd=5)
ent2.place(relx=0.35, rely=0.5, relwidth=0.3, anchor=W)

btn02 = Button(frm1, text="Today", bd= 5, command=set_today2)
btn02.place(relx=0.7, rely=0.5, relwidth=0.15, anchor=W)

lbl3 = Label(frm1, text="Result:", bg="gray60",  padx=10, pady=10,  justify=LEFT)
lbl3.place(relx=0.2, rely=0.6, anchor=W)
ent3 = Entry(frm1, textvariable=ent3_var, bd=5)
ent3.place(relx=0.35, rely=0.6, relwidth=0.3, anchor=W)

btn2 = Button(frm1, text="Reset", bd= 5, command=reset_main)
btn2.place(relx=0.7, rely=0.6, relwidth=0.15, anchor=W)

# =====================================================Buttons=====================================================
btn1 = Button(frm1, text="Total", bd= 5,  command=eval_date)
btn1.place(relx=0.35, rely=0.72, relwidth=0.3, relheight=0.1, anchor=W)

btn3 = Button(frm1, text="Exit", bd= 5, command=exit_main)
btn3.place(relx=0.7, rely=0.72, relwidth=0.15, relheight=0.1, anchor=W)

root.mainloop()