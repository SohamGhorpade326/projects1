from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Area Calculator")
root.geometry("900x700+200+60")
f = ("Arial", 20, "bold")
s = ("Roboto Slab", 30, "bold")
r=("Inter", 18)


def rect():
    length = ent_rect.get()
    breath = etn_rect.get()
    if (length == "") or (breath == ""):
        showerror("Issue", "Input cannot be empty")
        return
    for d in length:
        if not d.isdigit() and d != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_rect.delete(0, END)
            etn_rect.delete(0, END)
            ent_rect.focus()
            return
        if d == '-':
            showerror("Issue", "Input cannot be negative")
            ent_rect.delete(0, END)
            etn_rect.delete(0, END)
            ent_rect.focus()
            return
    for i in breath:
        if not i.isdigit() and i != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_rect.delete(0, END)
            etn_rect.delete(0, END)
            ent_rect.focus()
            return
        if i == '-':
            showerror("Issue", "Input cannot be negative")
            ent_rect.delete(0, END)
            etn_rect.delete(0, END)
            ent_rect.focus()
            return
    if float(length) < 0 or float(length) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        ent_rect.delete(0, END)
        etn_rect.delete(0, END)
        ent_rect.focus()
        return
    if float(breath) < 0 or float(breath) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        etn_rect.delete(0, END)
        ent_rect.delete(0, END)
        ent_rect.focus()
        return
    msg = "Area of Rectangle is " + str(round(float(length) * float(breath), 3)) + "  m² "
    lab_msg.config(text=msg, fg="blue")
    showinfo("Success", "Calculation successful")
    lab_msg.config(text=" ")
    ent_rect.delete(0, END)
    etn_rect.delete(0, END)
    ent_rect.focus()

def sqre():
    side = ent_sq.get()
    if side == "":
        showerror("Issue", "Input cannot be empty")
        return
    for d in side:
        if not d.isdigit() and d != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_sq.delete(0, END)
            ent_sq.focus()
            return
        if d == '-':
            showerror("Issue", "Input cannot be negative")
            ent_sq.delete(0, END)
            ent_sq.focus()
            return
    if float(side) < 0 or float(side) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        ent_sq.delete(0, END)
        ent_sq.focus()
        return
    msg = "Area of Square is " + str(round(float(side)*float(side), 3)) + "  m² "
    sq_msg.config(text=msg, fg="blue")
    showinfo("Success", "Calculation successful")
    sq_msg.config(text=" ")
    ent_sq.delete(0, END)
    ent_sq.focus()

def circle():
    radius = ent_cir.get()
    if radius == "":
        showerror("Issue", "Input cannot be empty")
        return
    for d in radius:
        if not d.isdigit() and d != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_cir.delete(0, END)
            ent_cir.focus()
            return
        if d == '-':
            showerror("Issue", "Input cannot be negative")
            ent_cir.delete(0, END)
            ent_cir.focus()
            return
    if float(radius) < 0 or float(radius) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        ent_cir.delete(0, END)
        ent_cir.focus()
        return
    msg = "Area of Circle is " + str(round(float(radius)*float(radius)*3.145, 3)) + "  m² "
    cir_msg.config(text=msg, fg="blue")
    showinfo("Success", "Calculation successful")
    cir_msg.config(text=" ")
    ent_cir.delete(0, END)
    ent_cir.focus()

def triangle():
    breath = ent_tri.get()
    height = etn_tri.get()
    if (breath == "") or (height == ""):
        showerror("Issue", "Input cannot be empty")
        return
    for d in breath:
        if not d.isdigit() and d != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_tri.delete(0, END)
            etn_tri.delete(0,END)
            ent_tri.focus()
            return
        if d == '-':
            showerror("Issue", "Input cannot be negative")
            ent_tri.delete(0, END)
            etn_tri.delete(0,END)
            ent_tri.focus()
            return
    for i in height:
        if not i.isdigit() and i != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_tri.delete(0, END)
            etn_tri.delete(0, END)
            ent_tri.focus()
            return
        if i == '-':
            showerror("Issue", "Input cannot be negative")
            ent_tri.delete(0, END)
            etn_tri.delete(0, END)
            ent_tri.focus()
            return
    if float(breath) < 0 or float(breath) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        ent_tri.delete(0, END)
        etn_tri.delete(0, END)
        ent_tri.focus()
        return
    if float(height) < 0 or float(height) > 1000:
        showerror("Issue", "Input must be between 0 and 1000")
        etn_tri.delete(0, END)
        ent_tri.delete(0, END)
        ent_tri.focus()
        return
    msg = "Area of Triangle is " + str(round(float(height) * float(breath)*0.5, 3)) + "  m² "
    tri_msg.config(text=msg, fg="blue")
    showinfo("Success", "Calculation successful")
    tri_msg.config(text=" ")
    ent_tri.delete(0, END)
    etn_tri.delete(0, END)
    ent_tri.focus()

lab_title = Label(root, text="T2v5 Area Converter", font=s, fg="red")
rect_title = Label(root, text="1. Area of Rectangle ", font=f, fg="purple")
lab_rect = Label(root, text="Enter Length(in meter): ", font=r)
ent_rect = Entry(root, font=r, width=10, borderwidth=3)
lba_rect = Label(root, text="Enter Breath(in meter): ", font=r)
etn_rect = Entry(root, font=r, width=10, borderwidth=3 )
btn_rect = Button(root, text="Calculate ", font=f, command=rect)
lab_msg = Label(root, font=f)
lab_title.place(x=600, y=30)
rect_title.place(x=70, y=150)
lab_rect.place(x=80, y=250)
ent_rect.place(x=420, y=250)
lba_rect.place(x=80, y=300)
etn_rect.place(x=420, y=300)
btn_rect.place(x=80, y=380)
lab_msg.place(x=250, y=380)

sq_title = Label(root, text="2. Area of Square ", font=f, fg="purple")
lab_sq = Label(root, text="Enter Side(in meter): ", font=r)
ent_sq = Entry(root, font=r, width=10, borderwidth=3)
btn_sq = Button(root, text="Calculate", font=f, command=sqre)
sq_msg = Label(root, font=f)
sq_title.place(x=800, y=150)
lab_sq.place(x=800, y=250)
ent_sq.place(x=1100, y=250)
btn_sq.place(x=800, y=330)
sq_msg.place(x=1000, y=330)

cir_title = Label(root, text="3. Area of Circle", font=f, fg="purple")
lab_cir = Label(root, font=r, text="Enter radius(in meter): ")
ent_cir = Entry(root, font=r, width=10, borderwidth=3)
btn_cir = Button(root, text="Calculate", font=f, command=circle)
cir_msg = Label(root, font=f)
cir_title.place(x=70, y=480)
lab_cir.place(x=80, y=560)
ent_cir.place(x=420, y=560)
btn_cir.place(x=80, y=630)
cir_msg.place(x=250, y=630)

tri_title = Label(root, text="4. Area of Triangle", font=f, fg="purple")
lab_tri = Label(root, font=r, text="Enter breath(in meter): ")
ent_tri = Entry(root, font=r, width=10, borderwidth=3)
lba_tri = Label(root, font=r, text="Enter height(in meter): ")
etn_tri = Entry(root, font=r, width=10, borderwidth=3)
btn_tri = Button(root, text="Calculate", font=f, command=triangle)
tri_msg = Label(root, font=f)
tri_title.place(x=800, y=480)
lab_tri.place(x=800, y=550)
ent_tri.place(x=1150, y=550)
lba_tri.place(x=800, y=600)
etn_tri.place(x=1150, y=600)
btn_tri.place(x=800, y=680)
tri_msg.place(x=1000, y=680)

root.mainloop()