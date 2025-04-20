#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox


# In[9]:


class hostelRegistration:
    def __init__(self, root):
        self.root = root
        self.root.title('Hostel Room Management System')
        self.root.geometry("1550x800+0+0")
        # ================= Create Var ========================
        self.email = tk.StringVar()
        self.father = tk.StringVar()
        self.name = tk.StringVar()
        self.day = tk.IntVar()
        self.month = tk.StringVar()
        self.year = tk.IntVar()
        self.roll = tk.StringVar()
        self.mother = tk.StringVar()
        self.mobile = tk.StringVar()  

        # =================== Title ============================
        lbl_title = tk.Label(self.root, text="Student Registration", font=("Times New Roman", 30, "bold"), bg="blue", fg="white", anchor='nw', padx=10)
        lbl_title.place(x=0, y=0, width=1550, height=50)

        # ==================== Frame ============================
        regi_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE)
        regi_frame.place(x=70, y=120, width=1150, height=520)

        # ===================== Form Title ============================
        form_title = tk.Label(self.root, text="Filling Your Detail", font=("Times New Roman", 30, "bold"), fg="red")
        form_title.place(x=490, y=50)

        # ==== Name field =========#
        name = tk.Label(regi_frame, text="Name", font=("Times New Roman", 15, "bold"))
        name.place(x=30, y=20)

        entry_name = tk.Entry(regi_frame, textvariable=self.name, width=30, font=('Times', 12))
        entry_name.place(x=30, y=50)

        # ==== Email field =========#
        Email = tk.Label(regi_frame, text="Email ID", font=("Times New Roman", 15, "bold"))
        Email.place(x=760, y=20)

        entry_email = tk.Entry(regi_frame, textvariable=self.email, width=40, font=('Times', 12))
        entry_email.place(x=760, y=50)

        # ==== Date of Birth fields ======#
        Dob = tk.Label(regi_frame, text="Date Of Birth", font=("Times New Roman", 15, "bold"))
        Dob.place(x=760, y=120)

        combo_day = ttk.Combobox(regi_frame, width=5, textvariable=self.day, font=('Times', 12), state='readonly')
        combo_day['values'] = ['Day'] + [int(i) for i in range(1, 32)]
        combo_day.current(0)
        combo_day.place(x=760, y=150)

        label_dash1 = tk.Label(regi_frame, text="-", font=("Times New Roman", 15))
        label_dash1.place(x=820, y=150)

        combo_month = ttk.Combobox(regi_frame, width=7, textvariable=self.month, font=('Times', 12), state='readonly')
        combo_month['values'] = ['Month'] + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        combo_month.current(0)
        combo_month.place(x=833, y=150)

        label_dash2 = tk.Label(regi_frame, text="-", font=("Times New Roman", 15))
        label_dash2.place(x=914, y=150)

        combo_year = ttk.Combobox(regi_frame, width=10, textvariable=self.year, font=('Times', 12), state='readonly')
        combo_year['values'] = ['Year'] + [int(i) for i in range(1980, 2051)]
        combo_year.current(0)
        combo_year.place(x=925, y=150)

        Roll = tk.Label(regi_frame, text="Enrolment No.", font=("Times New Roman", 15, 'bold'))
        Roll.place(x=760, y=220)

        entry_roll = tk.Entry(regi_frame, textvariable=self.roll, width=30, font=('Times', 12))
        entry_roll.place(x=760, y=250)

        Father = tk.Label(regi_frame, text="Father Name", font=("Times New Roman", 15, 'bold'))
        Father.place(x=30, y=120)

        entry_father = tk.Entry(regi_frame, textvariable=self.father, width=30, font=('Times', 12))
        entry_father.place(x=30, y=150)

        Mother = tk.Label(regi_frame, text="Mother Name", font=("Times New Roman", 15, 'bold'))
        Mother.place(x=760, y=320)

        entry_mother = tk.Entry(regi_frame, textvariable=self.mother, width=30, font=('Times', 12))
        entry_mother.place(x=760, y=350)

        Add = tk.Label(regi_frame, text="Address", font=("Times New Roman", 15, 'bold'))
        Add.place(x=30, y=270)

        self.entry_add = tk.Text(regi_frame, width=30, height=3, font=('Times', 12))
        self.entry_add.place(x=115, y=270)

        label_number = tk.Label(regi_frame, text="Your Mobile No :", font=("Times New Roman", 15, 'bold'))
        label_number.place(x=760, y=390)

        entry_number = tk.Entry(regi_frame, textvariable=self.mobile, width=30, font=('Times', 12))
        entry_number.place(x=760, y=420)

        # ==== Submit Button =======#
        login_btn = tk.Button(regi_frame, text="Click here to Register", command=self.entry_check, width=70, font=("Times New Roman", 13, "bold"), bg="red", fg="white", bd=0, cursor="hand1")
        login_btn.place(x=170, y=478)

    def entry_check(self):
        if self.email.get()=='' or self.father.get()=='' or self.entry_add.get("1.0", tk.END).strip() == '' or self.name.get()=='' or self.month.get()=='' or self.roll.get()=='' or self.mother.get()=='' or self.mobile.get()=='':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.day.get() == 0 or self.year.get() == 0:
            messagebox.showerror("Error", "Please select date and year", parent=self.root)
        else:
            try:
                mobile_number=self.mobile.get().strip()
                if not mobile_number.isdigit():
                  messagebox.showwarning("Invalid mobile number","Mobile number must contain only digit", parent=self.root)
                  return
                if len(mobile_number)!=10:
                  messagebox.showwarning("Invalid mobile number","Mobile number should be 10 digit", parent=self.root)
                  return
                mobile_int=int(mobile_number)
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Kashish@1234",
                    database="management"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Registration values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.email.get(),
                        self.father.get(),
                        self.entry_add.get("1.0", tk.END).strip(),
                        self.name.get(),
                        self.day.get(),
                        self.month.get(),
                        self.year.get(),
                        self.roll.get(),
                        self.mother.get(),
                        mobile_int
                    )
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your form is submitted", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


# In[10]:


if __name__=='__main__':
    root=tk.Tk()
    obj=hostelRegistration(root)
    root.mainloop()
    


# In[ ]:




