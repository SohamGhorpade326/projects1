from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Weight Converter")
root.geometry("900x700+200+60")
f = ("Arial", 30, "bold")

def show():
    name = ent_name.get()
    if name == "":
        showerror("Issue", "Input cannot be empty")
        return
    for d in name:
        if not d.isdigit() and d != '-':
            showerror("Issue", "Input cannot contain text or special characters")
            ent_name.delete(0, END)
            ent_name.focus()
            return
    
    if float(name) < 0 or float(name) > 100:
        showerror("Issue", "Input must be between 0 and 100")
        ent_name.delete(0, END)
        ent_name.focus()
        return
    if s.get() == 1:
        msg = round(float(name) * 0.453592, 3)
        mg = "Weight in kg: " + str(msg)
    else:
        msg = round(float(name) * 2.20462, 3)
        mg = "Weight in pounds: " + str(msg)
    lab_msg.config(text=mg, fg="blue")
    showinfo("Success", "Conversion successful")
    lab_msg.config(text=" ")
    ent_name.delete(0, END)
    ent_name.focus()

lab_title = Label(root, font=f, text="Weight Converter")
lab_name = Label(root, font=f, text="Enter Weight : ")
ent_name = Entry(root, font=f, width=12)

s = IntVar()
s.set(1)
rb_pod = Radiobutton(root, text="Pounds to Kg", font=f, variable=s, value=1)
rb_kg = Radiobutton(root, text="Kg to Pounds", font=f, variable=s, value=2)

btn_submit = Button(root, text="Convert", font=f, command=show)
lab_msg = Label(root, font=f)

lab_title.place(x=320, y=70)
lab_name.place(x=200, y=200)
ent_name.place(x=500, y=200)
rb_pod.place(x=150, y=350)
rb_kg.place(x=500, y=350)
btn_submit.place(x=400, y=450)
lab_msg.place(x=300, y=550)

root.mainloop()