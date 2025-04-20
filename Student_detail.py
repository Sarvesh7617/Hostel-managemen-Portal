#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk                           #inbuilt library 
import tkinter.ttk as ttk
from tkinter import messagebox
import mysql.connector


# In[2]:


class admin_table:
    def __init__(self, root):
        self.root = root
        self.root.title('Hostel Room Management System')
        self.root.geometry("1550x800+0+0")  # Window size
        
        # Button for Delete and Reset
        btnDelete = tk.Button(self.root, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnDelete.place(x=620, y=600)
        
        btnReset = tk.Button(self.root, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnReset.place(x=750, y=600)

        # Table Frame
        Table_Frame = tk.LabelFrame(self.root, bd=2, relief=tk.RIDGE, text="View Student Details", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=260, y=50, width=825, height=490)
        
        details_table = tk.Frame(Table_Frame, bd=2, relief=tk.RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)
        
        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=tk.VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("Student_name", "Father_name", "Mother_name", "Mobile_no", "Email", "Address", "Hostel", "DOB", "Enrollment_no", "Room_no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side='bottom', fill='x')  # Change BOTTOM to 'bottom'
        scroll_y.pack(side='right', fill='y')   # This is fine as 'right' is correct
        
        # Column configuration for Treeview
        self.Cust_Details_Table.heading("Student_name", text="Student Name")
        self.Cust_Details_Table.heading("Father_name", text="Father Name")
        self.Cust_Details_Table.heading("Mother_name", text="Mother Name")
        self.Cust_Details_Table.heading("Mobile_no", text="Mobile No.")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("Address", text="Address")
        self.Cust_Details_Table.heading("Hostel", text="Hostel")
        self.Cust_Details_Table.heading("DOB", text="Date of Birth")
        self.Cust_Details_Table.heading("Enrollment_no", text="Enrollment No.")
        self.Cust_Details_Table.heading("Room_no", text="Room No.")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.pack(fill=tk.BOTH, expand=True)
        
        # Fetch and display data from Student_detail table
        self.fetch_data()

    def fetch_data(self):
        # Connect to the database
        conn = mysql.connector.connect(host="localhost", user="root", password="Kashish@1234", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Student_detail")  # Fetch from Student_detail table
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                dob = row[4]  # Assuming DOB is stored as 'DD-Month-YYYY' in the Student_detail table
                self.Cust_Details_Table.insert("", tk.END, values=row[:4] + (dob,) + row[5:])
            conn.commit()
        conn.close()


# In[3]:


if __name__=='__main__':
    root=tk.Tk()
    obj=admin_table(root)
    root.mainloop()


# In[ ]:




