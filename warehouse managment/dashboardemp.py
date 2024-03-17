import time
from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
import sqlite3

import os
from tkinter import messagebox


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("warehouse managment")
        self.root.config(bg="gray")
        # --------------title
        self.icon_title = PhotoImage(file="images\cart.png")

        title = Label(self.root, text="WELOCOME TO WAREHOUSE MANAGEMENT", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 30, "bold"), bg="yellow", fg="black", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        # ----button
        btn_logout = Button(self.root, text="LOGOUT", command=self.logout, font=(
            "times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1100, y=10, height=30, width=150)
        # ==clock===
        self.lbl_clock = Label(self.root, text="welcome to warehouse\t\t date:DD-MM-YYYY\t\t time :HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ----left menu
        self.Menulogo = Image.open("images/flip.png")
        self.Menulogo = self.Menulogo.resize((200, 200), Image.ANTIALIAS)
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        self.icon_side = PhotoImage(file="images/ar.png")

        lbl_menuLogo = Label(LeftMenu, image=self.Menulogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=(
            "times new roman", 20), bg="blue").pack(side=TOP, fill=X)

        # btn_employee = Button(LeftMenu, text="employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
        #    "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="supplier",  command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="category", command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="product", command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        # btn_sales = Button(LeftMenu, text="sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
        #     "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="exit", image=self.icon_side, compound=LEFT, command=self.exit, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="light blue", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # --------------------content
        self.lbl_employee = Label(self.root, text="total employee", bd=5, relief=RIDGE,
                                  bg="green", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="total supplier", bd=5, relief=RIDGE,
                                  bg="red", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="total category", bd=5, relief=RIDGE,
                                  bg="orange", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="total product", bd=5, relief=RIDGE,
                                 bg="purple", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        # self.lbl_sales = Label(self.root, text="total sales", bd=5, relief=RIDGE,
        #                        bg="gray", fg="white", font=("goudy old style", 20, "bold"))
        # self.lbl_sales.place(x=650, y=300, height=150, width=300)

        self.update_content()

        # ---------footer
        lbl_footer = Label(self.root, text="mangement powered by SP\n project",
                           font=("times new roman", 10), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        # lbl_footer.place(x=0, y=70, relwidth=1, height=30)
        # =========================================

    # def employee(self):
    #     self.new_win = Toplevel(self.root)
    #     self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def exit(self):
        self.root.destroy()

    # def sales(self):
    #     self.new_win = Toplevel(self.root)
    #     self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from product")
            product = cur.fetchall()
            self.lbl_product.config(
                text=f'total product \n[{str(len(product))}]')

            cur.execute("select *from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(
                text=f'total supplier \n[{str(len(supplier))}]')

            cur.execute("select *from category")
            category = cur.fetchall()
            self.lbl_category.config(
                text=f'total category \n[{str(len(category))}]')

            cur.execute("select count(*) from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(
                text=f'total employee \n [{str(len(category))}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(
                text=f"welcome to warehouse mangement \t\t date:{str(date_)}\t\t time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
