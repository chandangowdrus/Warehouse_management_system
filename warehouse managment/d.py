from tkinter import *
import tkinter as tk
from tkinter import ttk
# from dashbord import IMS
from employee import employeeClass
import sqlite3
import os
# from tkinter import messageboxs
# defining login function


def login():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    uname = username.get()
    pwd = password.get()
    print(uname, pwd)
    try:
        print("in try")
        if uname == '' or pwd == '':
            message.set("fill the empty field!!!")
        else:
            print("in try else")
            cur.execute(
                "select *from employee where eid=? AND pass=?", (uname, pwd))
            user = cur.fetchone()

            if user == None:
                message.set("incorrect user id or password")
            else:
                login_screen.destroy()
                os.system("python dashboard.py")
                message.set("login successful")

    except Exception as ex:
        message.set(ex)
# defining loginform function


def Loginform():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    login_screen.geometry("1350x700")
    # declaring variable
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    utype = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Please enter EMPLOYEE id and PASSWORD ",
          bg="orange", fg="white").pack()
    Label(login_screen, text="WELOCOME TO WAREHOUSE MANAGEMENT",
          font=("goudy old style", 20, "bold")).place(x=350, y=100)
    # Username Label
    Label(login_screen, text="employee id * ").place(x=500, y=200)
    # Username textbox
    Entry(login_screen, textvariable=username).place(x=600, y=200)
    # Password Label
    Label(login_screen, text="Password * ").place(x=500, y=250)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*").place(x=600, y=250)
    # Label for displaying login status[success/failed]
    # Label(login_screen, text="", textvariable=message).place(x=550, y=300)

    # ttk.Combobox(login_screen, text="", values=("Admin", "employee"),
    #             textvariable = utype).place(x = 590, y = 300)

    # Login button
    Button(login_screen, text="Login", width=10, height=1,
           bg="orange", command=login).place(x=570, y=350)
    login_screen.mainloop()


# calling function Loginform
Loginform()
