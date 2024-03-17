# till part 2  22:0 out of 56:41
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class employeeClass:
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

        self.var_emp_id = StringVar()
        self.var_contact = StringVar()
        self.var_gender = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        # --------------searchbox
        SearchFrame = LabelFrame(self.root, text="search employee", font=(
            "times new roman", 14, "bold"), bd=1, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # --------------option
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=(
            "select", "Email", "Name", "contact"), state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=(
            "goudy old style", 12), bg="light yellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="search", font=(
            "goudy old style", 13), bg="green", fg="white", command=self.search, cursor="hand2").place(x=390, y=8, width="150", height="25")

        # --title
        title = Label(self.root, text="Employee details", font=(
            "goudy old style", 12, "bold"), bg="#0f4d7d", fg="white").place(x=50, y=100, width="1000")

        # -----------content
        # ---------------------row1
        label_epmid = Label(self.root, text="Employee ID", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=150)
        label_gender = Label(self.root, text="Gender", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=350, y=150)
        label_contact = Label(self.root, text="Contact", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=750, y=150)

        txt_epmid = Entry(self.root, textvariable=self.var_emp_id, font=(
            "goudy old style", 12, "bold"), bg="white").place(x=150, y=150, width=180)
        txt_gender = Entry(self.root, textvariable=self.var_gender, font=(
            "goudy old style", 12, "bold"), bg="white").place(x=420, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=(
            "select", "male", "female", "other"), state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_gender.place(x=420, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "goudy old style", 12, "bold"), bg="white").place(x=830, y=150, width=180)

        # --------------------row 2
        label_name = Label(self.root, text="Ename", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=190)
        label_dob = Label(self.root, text="DOB", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=350, y=190)
        label_doj = Label(self.root, text="DOJ", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=400, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=790, y=190, width=180)

        # --------------------row 3
        label_email = Label(self.root, text="email", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=230)
        label_pass = Label(self.root, text="password", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=350, y=230)
        label_utype = Label(self.root, text="user type", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=450, y=230, width=180)
        txt_utype = Entry(self.root, textvariable=self.var_utype, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=850, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=(
            "admin", "employee"), state='readonly', justify=CENTER, font=(
            "times new roman", 12))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # --------------------row 4
        label_address = Label(self.root, text="address", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=50, y=270)
        label_salary = Label(self.root, text="salary", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=500, y=270)

        txt_address = Entry(self.root, textvariable=self.var_address, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=(
            "goudy old style", 12, "bold"), bg="light yellow").place(x=600, y=270, width=180)

        # ====button==
        btn_add = Button(self.root, text="add", command=self.add, font=(
            "goudy old style", 13), bg="green", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="update", command=self.update, font=(
            "goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="delete", font=(
            "goudy old style", 13), bg="red", fg="white", command=self.delete, cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="clear", font=(
            "goudy old style", 13), bg="gray", fg="white", command=self.clear, cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ======emplyee details

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.Employeetable = ttk.Treeview(emp_frame, columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Employeetable.xview)
        scrolly.config(command=self.Employeetable.yview)

        self.Employeetable.heading("eid", text="EMP ID")
        self.Employeetable.heading("name", text="name")
        self.Employeetable.heading("email", text="email")
        self.Employeetable.heading("gender", text="gender")
        self.Employeetable.heading("contact", text="contact")
        self.Employeetable.heading("dob", text="DOB")
        self.Employeetable.heading("doj", text="DOJ")
        self.Employeetable.heading("pass", text="pass")
        self.Employeetable.heading("utype", text="utype")
        self.Employeetable.heading("address", text="address")
        self.Employeetable.heading("salary", text="salary")
        self.Employeetable["show"] = "headings"

        self.Employeetable.column("eid", width=90)
        self.Employeetable.column("name", width=90)
        self.Employeetable.column("email", width=90)
        self.Employeetable.column("gender", width=90)
        self.Employeetable.column("contact", width=90)
        self.Employeetable.column("dob", width=90)
        self.Employeetable.column("doj", width=90)
        self.Employeetable.column("pass", width=90)
        self.Employeetable.column("utype", width=90)
        self.Employeetable.column("address", width=90)
        self.Employeetable.column("salary", width=90)
        self.Employeetable["show"] = "headings"

        self.Employeetable.pack(fill=BOTH, expand=1)
        self.Employeetable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


# =======================================================================


    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "error", "employee ID must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "error", "Employee alreday exits,try another", parent=self.root)
                else:
                    cur.execute("insert into employee(eid ,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_address.get(),
                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "employee added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select *from employee")
            rows = cur.fetchall()
            self.Employeetable.delete(*self.Employeetable.get_children())
            for row in rows:
                self.Employeetable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.Employeetable.focus()
        content = (self.Employeetable.item(f))
        row = content['values']
        print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.var_address.set(row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "error", "employee ID must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid emp id", parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where  eid =?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_address.get(),
                        self.var_salary.get(),
                        self.var_emp_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "success", "employee updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "error", "employee ID must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "error", "invalid emp id", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "r u sure you want to delete")
                    if op == True:
                        cur.execute("delete from employee where eid=?",
                                    (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "delelte", "employee deleted successfully", parent=self.root)
                        # self.show()
                        self.clear()

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.var_address.set("")
        self.var_salary.set("")
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
                cur.execute("select *from employee where "+self.var_searchby.get() +
                            " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Employeetable.delete(
                        *self.Employeetable.get_children())
                    for row in rows:
                        self.Employeetable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "error", "no record", parent=self.root)

        except Exception as ex:
            messagebox.showerror(
                "error", f"error due to :{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
