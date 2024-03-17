# till part 2  22:0 out of 56:41
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


class supplierClass:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("warehouse managment")
        self.root.config(bg="white")
        self.root.focus_force()
        # ===========
        # All variaable
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_desc = StringVar()

        # --------------searchbox

        # --------------option
        lbl_search = Label(self.root, text="search by invoice number", font=(
            "times new roman", 12, "bold"))
        lbl_search.place(x=700, y=70)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=(
            "goudy old style", 12), bg="light yellow").place(x=700, y=100)
        btn_search = Button(self.root, text="search", command=self.search, font=(
            "goudy old style", 13), bg="green", fg="white", cursor="hand2").place(x=900, y=100, width="150", height="25")

        # --title
        title = Label(self.root, text="Supplier details", font=(
            "goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").place(x=50, y=10, width="1000", height=40)

        # -----------content
        # ---------------------row1
        label_supplier_invoice = Label(self.root, text="Invoice No.", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=(
            "goudy old style", 12, "bold"), bg="white").place(x=180, y=80, width=180)

        # --------------------row 2
        label_name = Label(self.root, text="Name", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=120, width=180)

        # --------------------row 3
        label_contact = Label(self.root, text="Contact", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=160, width=180)

        # --------------------row 4
        label_desc = Label(self.root, text="Description", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=200)
        txt_desc = Entry(self.root, textvariable=self.var_desc, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=200, width=300, height=100)

        # ====button==
        btn_add = Button(self.root, text="add", command=self.add, font=(
            "goudy old style", 13), bg="green", fg="white", cursor="hand2").place(x=180, y=370, width=110, height=28)
        btn_update = Button(self.root, text="update", command=self.update, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=300, y=370, width=110, height=28)
        btn_delete = Button(self.root, text="delete", command=self.delete, font=(
            "goudy old style", 13), bg="red", fg="white", cursor="hand2").place(x=420, y=370, width=110, height=28)
        btn_clear = Button(self.root, text="clear", command=self.clear, font=(
            "goudy old style", 13), bg="gray", fg="white", cursor="hand2").place(x=540, y=370, width=110, height=28)

        # ======emplyee details

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700, y=140, width=380, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=(
            "Invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("Invoice", text="INVOICE")
        self.supplierTable.heading("name", text="NAME")
        self.supplierTable.heading("contact", text="CONTACT")
        self.supplierTable.heading("desc", text="DESCRIPTION")
        self.supplierTable["show"] = "headings"

        self.supplierTable.column("Invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=90)
        self.supplierTable["show"] = "headings"

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
# =========================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "error", "invoice number must be required ", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "error", "invoice number alreday exits,try another", parent=self.root)
                else:
                    cur.execute("insert into supplier(invoice ,name,contact,desc)values(?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "supplier added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_desc.set(row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "error", "invoice number  must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid emp id", parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? where  invoice =?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(),
                        self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "suppler updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "error", "invoice number must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid invoice", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "r u sure you want to delete")
                    if op == True:
                        cur.execute("delete from supplier where invoice=?",
                                    (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "delelte", "supplier deleted successfully", parent=self.root)
                        # self.show()
                        self.clear()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.set("")
        self.var_searchtxt.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if (self.var_searchtxt.get() == "select"):
                messagebox.showerror(
                    "error", "invoice  number required", parent=self.root)
            else:
                cur.execute("select *from supplier where invoice =? ",
                            (self.var_searchtxt.get(),))
                row = cur.fetchall()
                if row != None:
                    self.supplierTable.delete(
                        *self.supplierTable.get_children())
                    for row in row:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "error", "no record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
