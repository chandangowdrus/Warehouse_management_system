import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

import sqlite3
import os


def login():
    employee_id = employee_id_entry.get()
    password = password_entry.get()
    user_type = user_type_var.get()
    if not employee_id or not password or not user_type:
        messagebox.showerror("Error", "Please fill all fields")
    else:

        conn = sqlite3.connect(database=r'ims.db')
        c = conn.cursor()
        c.execute("SELECT utype FROM employee WHERE email=? AND pass=?",
                  (employee_id, password))
        result = c.fetchone()
        if result:
            if result[0] == 'admin' and user_type == 'admin':
                messagebox.showinfo("Success", "Admin login successful.")
                root.destroy()
                os.system("python dashboard.py")
            elif result[0] == 'employee' and user_type == 'employee':
                messagebox.showinfo("Success", "Employee login successful.")
                root.destroy()
                os.system("python dashboardemp.py")
            else:
                messagebox.showerror("Error", "Invalid User Type")
        else:
            messagebox.showerror("Error", "Invalid login")
        conn.close()


root = tk.Tk()
root.geometry("1250x700+0+0")
root.title("Warehouse Login")
image = PhotoImage(file="images/bg.ppm")

# Create a label widget to display the image
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title = tk.Label(
    root, text="WELCOME TO WAREHOUSE MANAGEMENT", font=("Arial", 18, 'bold'))
title.place(x=400, y=10)

title_d = tk.Label(
    root, text="please enter the valid email and password", font=("Arial", 13))
title_d.place(x=470, y=100)

employee_id_label = tk.Label(
    root, text="EMAIL ID:", font=("Arial", 12))
employee_id_label.place(x=450, y=200)

employee_id_entry = tk.Entry(root, font=("Arial", 12), bg='light yellow')
employee_id_entry.place(x=650, y=200)

password_label = tk.Label(root, text="PASSWORD:", font=("Arial", 12))
password_label.place(x=450, y=250)

password_entry = tk.Entry(
    root, show="*", font=("Arial", 12), bg='light yellow')
password_entry.place(x=650, y=250)

user_type_var = tk.StringVar(value="employee")
user_type_dropdown = tk.OptionMenu(root, user_type_var, "employee", "admin")
user_type_dropdown.config(font=("Arial", 12))
user_type_dropdown.place(x=650, y=300)

login_button = tk.Button(root, text="Login", font=(
    "Arial", 12), bg='light green', command=login)
login_button.place(x=600, y=370)

# Create an image object

root.mainloop()