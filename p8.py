from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
    name = ent_name.get()
    password = ent_pass.get()
    if (name == "SOHAM") and (password == "1234"):
        mw.withdraw()
        aw.deiconify()
    else:
        showerror("issue", "login failed")
        ent_name.delete(0, END)
        ent_pass.delete(0, END)
        ent_name.focus()

def f2():
    aw.withdraw()
    vw.deiconify()

def f3():
    if vw_ent_rno.get() == "":
        showerror("issue", "rno is empty")
        vw_ent_rno.focus()
        return

    con = None
    try:
        con = connect("ck.db")
        cursor = con.cursor()
        sql = "insert into student values(?,?,?,?,?,?)"
        rno = int(vw_ent_rno.get())
        if rno < 1:
            showerror("issue", "rno should be min 1")
            vw_ent_rno.focus()
            return

        name = vw_ent_name.get()
        if name == "":
            showerror("issue", "name cannot be empty")
            vw_ent_name.focus()
            return
        if not name.isalpha():
            showerror("issue", "name should contain only alphabets")
            vw_ent_name.delete(0, END)
            vw_ent_name.focus()
            return
        if len(name) < 0 or len(name) > 50:
            showerror("issue", "name: limit is between 0 to 50 ")
            vw_ent_name.focus()
            return
        
        phone = vw_ent_phone.get()
        if phone == "":
            showerror("Issue", "phone no cannot be empty")
            return
        for d in phone:
            if not d.isdigit() and d != '-':
                showerror("Issue", "phone no cannot contain text or special characters")
                vw_ent_phone.delete(0, END)
                return
            if d == "-":
                showerror("Issue", "phone no cannot be negative ")
                vw_ent_phone.delete(0, END)
                return
        if len(phone) < 0 or len(phone) > 11:
            showerror("Issue", "phone no must be between 0 and 10")
            vw_ent_phone.delete(0, END)
            vw_ent_phone.focus()
            return
        
        email = vw_ent_address.get()
        if email == "":
            showerror("issue", "email address cannot be empty")
            vw_ent_address.focus()
            return
        if len(email) < 0 or len(email) > 15:
            showerror("issue", "email address: limit is between 0 to 15 ")
            vw_ent_address.focus()
            return
        
        delivery = vw_ent_delivery.get()
        if delivery == "":
            showerror("issue", "delivery address cannot be empty")
            vw_ent_delivery.focus()
            return
        for d in delivery:
             if not (d.isalpha() or d == " "):
                 showerror("issue", "delivery address should contain only alphabets")
                 vw_ent_delivery.delete(0, END)
                 vw_ent_delivery.focus()
                 return
        if len(delivery) < 0 or len(delivery) > 50:
            showerror("issue", "delivery address: limit is between 0 to 100 ")
            vw_ent_delivery.focus()
            return
        
        beverage = ""
        if a.get() == 1:
            beverage = beverage + " Tea "
        if j.get() == 1:
            beverage = beverage + " Coffee "
        if o.get() == 1:
            beverage = beverage + " Juice "
        if c.get() == 1:
            beverage = beverage + " Milkshake "
        if x.get() == 1:
            beverage = beverage + " Soda "
        
        cursor.execute(sql, (rno, name, phone, email, delivery, beverage))
        con.commit()
        showinfo("success", "record created")
        vw_ent_rno.delete(0, END)
        vw_ent_name.delete(0, END)
        vw_ent_phone.delete(0, END)
        vw_ent_delivery.delete(0, END)
        vw_ent_address.delete(0, END)
        vw_ent_rno.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def f4():
    vw.withdraw()
    aw.deiconify()

def f5():
    dw.withdraw()
    aw.deiconify()

def f6():
    vw.withdraw()
    dw.deiconify()
    dw_st_data.delete(1.0, END)
    con = None
    try:
        con = connect("ck.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info += f"  rno= {d[0]}, name= {d[1]},  phone= {d[2]},  email address= {d[3]}, delivery address= {d[4]},  beverage= {d[5]}.\n"
        dw_st_data.insert(INSERT, info)
    except Exception as e:
        con.rollback()
        showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def f7():
    aw.withdraw()
    ew.deiconify()

def f8():
    try:
        con = connect("ck.db")
        cursor = con.cursor()
        sql = "delete from student where rno=?"
        rollno=ew_ent_name.get()
        if rollno=="":
            showerror("issue", " you have entered nothing ")
            ew_ent_name.focus()
            return
        if not rollno.isdigit():
            showerror("Issue", "roll no cannot contain text or special characters")
            ew_ent_name.delete(0, END)
            ew_ent_name.focus()
            return
        rno = int(ew_ent_name.get())
        cursor.execute(sql, (rno,))
        if cursor.rowcount == 0:
            raise ValueError("Record not found")
        con.commit()
        showinfo("success", "record deleted")
        ew_ent_name.delete(0, END)
        ew_ent_name.focus()
    except ValueError as ve:
        con.rollback()
        showerror("issue", "record not found ")
        ew_ent_name.delete(0, END)
        ew_ent_name.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", f"An error occurred: {str(e)}")
        ew_ent_name.delete(0, END)
        ew_ent_name.focus()
    finally:
        if con is not None:
            con.close()

def f9():
    ew.withdraw()
    aw.deiconify()

def f10():
    aw.withdraw()
    mw.deiconify()

mw = Tk()
mw.title("login")
mw.geometry("800x700+50+50")
f = ("Arial", 30, "bold")
mw.config(bg="yellow")

lab_title=Label(mw, text="Order Management System ", fg="green", bg="yellow",font=f)
lab_name = Label(mw, font=f,bg="yellow", text="Enter name: ")
ent_name = Entry(mw, font=f, width=12)
lab_pass = Label(mw, font=f, bg="yellow", text="Enter password: ")
ent_pass = Entry(mw, font=f, width=12)
btn_save = Button(mw, text="Login ", font=f, command=f1)
lab_title.pack(pady=10)
lab_name.pack(pady=25)
ent_name.pack(pady=27)
lab_pass.pack(pady=33)
ent_pass.pack(pady=35)
btn_save.pack(pady=42)

aw = Toplevel()
aw.title("Add/view/delete")
aw.attributes("-fullscreen", True)
f = ("Arial", 30, "bold")
aw.config(bg="light yellow")

btn_add = Button(aw, text="ADD Details", fg="purple",font=f, command=f2)
btn_view = Button(aw, text="View Details", fg="blue",font=f, command=f6)
btn_delete = Button(aw, text="Delete Details", fg="red", font=f, command=f7)
btn_back = Button(aw, text="Exit ", font=f, command=f10)
btn_add.pack(pady=20)
btn_view.pack(pady=30)
btn_delete.pack(pady=40)
btn_back.pack(pady=50)
aw.withdraw()

vw = Toplevel()
vw.title("Add Student")
vw.attributes("-fullscreen", True)
vw.config(bg="light yellow")

a = IntVar()
j = IntVar()
o = IntVar()
c = IntVar()
x = IntVar()
vw_rno = Label(vw, text="Enter Roll no: ", bg="light yellow", font=f)
vw_ent_rno = Entry(vw, font=f)
vw_name = Label(vw, text="Enter Name: ",bg="light yellow", font=f)
vw_ent_name = Entry(vw, font=f)
vw_phone = Label(vw, text="Enter Phone no:  ",bg="light yellow", font=f)
vw_ent_phone = Entry(vw, font=f)
vw_address = Label(vw, text="Enter Email Address:  ",bg="light yellow", font=f)
vw_ent_address = Entry(vw, font=f)
vw_delivery = Label(vw, text="Enter Delivery Address:  ", bg="light yellow", font=f)
vw_ent_delivery = Entry(vw, font=f)
vw_tea = Checkbutton(vw, text="Tea", font=f,bg="light yellow", variable=a)
vw_coff = Checkbutton(vw, text="Coffee", font=f, bg="light yellow", variable=j)
vw_jui = Checkbutton(vw, text="Juice", font=f, bg="light yellow", variable=o)
vw_milk = Checkbutton(vw, text="Milkshake", font=f, bg="light yellow", variable=c)
vw_soda = Checkbutton(vw, text="Soda", font=f,bg="light yellow", variable=x)
vw_btn = Button(vw, text="Save ", font=f, command=f3)
vw_back = Button(vw, text="Back ", font=f, command=f4)
vw_rno.place(x=50, y=50)
vw_ent_rno.place(x=400, y=50)
vw_name.place(x=50, y=120)
vw_ent_name.place(x=400, y=120)
vw_phone.place(x=50, y=200)
vw_ent_phone.place(x=400, y=200)
vw_address.place(x=50, y=270)
vw_ent_address.place(x=500, y=270)
vw_delivery.place(x=50, y=350)
vw_ent_delivery.place(x=500, y=350)
vw_tea.place(x=60, y=400)
vw_coff.place(x=60, y=450)
vw_jui.place(x=60, y=500)
vw_milk.place(x=60, y=550)
vw_soda.place(x=60, y=600)
vw_btn.place(x=400, y=680)
vw_back.place(x=600, y=680)
vw.withdraw()

dw = Toplevel()
dw.title("View Student")
dw.attributes("-fullscreen", True)
s = ("Arial", 20)
dw.config(bg="light yellow")

dw_st_data = ScrolledText(dw, font=s, width=100, height=20)
dw_btn_back = Button(dw, font=s, text="Back To Main",fg="red", command=f5)
dw_st_data.pack(pady=10)
dw_btn_back.pack(pady=10)

dw.withdraw()
ew = Toplevel()
ew.title("Delete Student")
ew.attributes("-fullscreen", True)
ew.config(bg="light yellow")

ew_name = Label(ew, text="Enter roll no: ", bg="light yellow", font=f)
ew_ent_name = Entry(ew, font=f, width=12)
ew_btn = Button(ew, text="Delete ", font=f, command=f8)
ew_back = Button(ew, text="Back ", font=f, command=f9)
ew_name.place(x=400, y=250)
ew_ent_name.place(x=700, y=250)
ew_btn.place(x=500, y=350)
ew_back.place(x=500, y=450)
ew.withdraw()
mw.mainloop()