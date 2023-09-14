from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
w=Tk()
w.geometry("300x300")
w.title("Rgistrstion...")
def add ():
    a=name.get()
##    conn=sqlite3.connect("regi.db")
##    conn.execute("create tabel user(name VarChar)")
##    print("created")
    conn.execute("insert into user (a)values (?),(a)")
lab_1=Label(w,text="name :",fg="blue",font=("bold",15))
lab_1.place(x=50,y=90)
ntry_1=Entry(bd=5,width=20)
ntry_1.place(x=150,y=90)
s=Button(w,text="click",command=add)
s.pack(side="bottom")
conn=sqlite3.connect("regi.db")
conn.execute("CREATE TABLE  if not exists user('name text')")
print("created")
w.mainloop()
