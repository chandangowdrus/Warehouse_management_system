import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("warehouse managment")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_invoice = StringVar()
        # title====
        lbl_tittle = Label(self.root, text="customer bill area", font=(
            "goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        lab_invoice = Label(self.root, text="invoice", font=(
            "times new roman", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=(
            "times new roman", 15), bg="light yellow").place(x=160, y=100, width=180, height=28)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
