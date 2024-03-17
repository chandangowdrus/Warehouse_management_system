import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("warehouse managment")
        self.root.config(bg="white")
        self.root.focus_force()
        # ==================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=450, height=480)

        # --title
        title = Label(product_Frame, text="product details", font=(
            "goudy old style", 18, "bold"), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)
        # -------------col 1

        lab_category = Label(product_Frame, text="category", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=60)
        lab_supplier = Label(product_Frame, text="supplier", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=110)
        lab_product = Label(product_Frame, text="product", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=160)
        lab_price = Label(product_Frame, text="price", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=210)
        lab_qty = Label(product_Frame, text="qty", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=260)
        lab_status = Label(product_Frame, text="status", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=310)

        # -------------------col 2
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_cat.place(x=150, y=65, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_sup.place(x=150, y=115, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name,  font=(
            "times new roman", 15), bg="light yellow").place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price,  font=(
            "times new roman", 15), bg="light yellow").place(x=150, y=210, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty,  font=(
            "times new roman", 15), bg="light yellow").place(x=150, y=260, width=200)

        cmd_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=(
            "active", "inactive"), state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmd_status.place(x=150, y=310, width=200)
        cmd_status.current(0)

        # ====button==
        btn_add = Button(product_Frame, text="add", command=self.add, font=(
            "goudy old style", 13), bg="green", fg="white", cursor="hand2").place(x=10, y=400, width=90, height=40)
        btn_update = Button(product_Frame, text="update", command=self.update, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=90, height=40)
        btn_delete = Button(product_Frame, text="delete", font=(
            "goudy old style", 13), bg="red", fg="white", command=self.delete, cursor="hand2").place(x=230, y=400, width=90, height=40)
        btn_clear = Button(product_Frame, text="clear", font=(
            "goudy old style", 13), bg="gray", fg="white", command=self.clear, cursor="hand2").place(x=340, y=400, width=90, height=40)

        # --------------searchbox
        SearchFrame = LabelFrame(self.root, text="search product", font=(
            "times new roman", 14, "bold"), bd=1, relief=RIDGE, bg="white")
        SearchFrame.place(x=480, y=10, width=600, height=80)

        # --------------option
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=(
            "Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=(
            "goudy old style", 12), bg="light yellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="search", font=(
            "goudy old style", 13), bg="green", fg="white", command=self.search, cursor="hand2").place(x=390, y=8, width="150", height="25")

        # ======product details

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame, columns=(
            "pid", "Supplier", "Category", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="pid")
        self.product_table.heading("Category", text="category")
        self.product_table.heading("Supplier", text="supplier")
        self.product_table.heading("name", text="name")
        self.product_table.heading("price", text="price")
        self.product_table.heading("qty", text="qty")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Category", width=90)
        self.product_table.column("Supplier", width=90)
        self.product_table.column("name", width=90)
        self.product_table.column("price", width=90)
        self.product_table.column("qty", width=90)
        self.product_table.column("status", width=90)

        # self.product_table["show"] = "headings"

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # -------------------------option

    def fetch_cat_sup(self):
        self.cat_list.append("empty")
        self.sup_list.append("empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()

        try:
            cur.execute("select name from category ")
            cat = cur.fetchall()
            self.cat_list.append("empty")
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "select" or self.var_cat.get() == "empty" or self.var_sup.get() == "select" or self.var_name.get() == "":
                messagebox.showerror(
                    "error", "all fields  must be required", parent=self.root)
            else:
                cur.execute("select * from product where name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "error", "product exits,try another", parent=self.root)
                else:
                    cur.execute("insert into product(Category, Supplier, name, price, qty, status)values(?,?,?,?,?,?)", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),


                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "product added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[2]),
        self.var_sup.set(row[1]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),

        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "error", "pls select product from  list", parent=self.root)
            else:
                cur.execute("select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid product", parent=self.root)
                else:
                    cur.execute("update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where  pid =?", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),


                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()


                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "product updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "error", " select product from list", parent=self.root)
            else:
                cur.execute("select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid product", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "r u sure you want to delete")
                    if op == True:
                        cur.execute("delete from product where pid=?",
                                    (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "delelte", "product deleted successfully", parent=self.root)
                        # self.show()
                        self.clear()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")

        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "select":
                messagebox.showerror(
                    "error", "select search by option", parent=self.root)
            elif (self.var_searchby.get() == ""):
                messagebox.showerror(
                    "error", "select input required", parent=self.root)
            else:
                cur.execute("select *from product where "+self.var_searchby.get() +
                            " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(
                        *self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "error", "no record", parent=self.root)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
