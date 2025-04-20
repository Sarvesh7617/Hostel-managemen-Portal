#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Student_detail import admin_table 


# In[8]:


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login Page")
        self.root.geometry("350x460+430+110")
        
        # Your database connection setup
        self.db_connection = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="Kashish@1234", 
            database="management"
        )
        self.db_cursor = self.db_connection.cursor()
        
        frame = tk.Frame(self.root, bg="black")
        frame.place(x=0, y=0, width=340, height=450)
        
        img1 = Image.open(r"D:\project\Hostel DBMS\Image\login.webp")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        
        lblimg1 = tk.Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=134, y=10, width=100, height=100)
        
        get_str = tk.Label(frame, text="Get Started", font=("times new roman", 28, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)
        
        # Username and Password Fields
        username = lbl = tk.Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=60, y=155)
        
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)
        
        password = lbl = tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)
        
        # Login Button
        loginbtn = tk.Button(frame, command=self.admin_Login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=tk.RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)
        
        # Register and Forget Password Button
        registerbtn = tk.Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)
        
        registerbtn = tk.Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=370, width=160)
    
    def admin_Login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Dbms project" and self.txtpass.get() == "Dbms@1234":
            messagebox.showinfo("Success", "Login Successful. Fetching student data...")
            self.populate_student_detail()
        else:
            messagebox.showerror("Invalid", "Invalid username or password")
    
    def populate_student_detail(self):
        # Query Registration and Room_book tables for student data
        query = """
        SELECT r.email_id, r.father_name, r.address, r.name, r.dob_day, r.dob_month, r.dob_year, r.enrol_no, r.mother_name, r.mobile_no, 
               rb.select_hostel, rb.room_block, rb.room_no
        FROM Registration r
        INNER JOIN Room_book rb ON r.mobile_no = rb.mobile_no
        """
        
        self.db_cursor.execute(query)  # Execute query
        result = self.db_cursor.fetchall()  # Fetch all matching rows
        
        if result:
            for row in result:
                # Format dob_day, dob_month, dob_year into appropriate strings
                dob_day = f"{row[4]:02d}"  # Ensure day is two digits
                dob_month = row[5]  # Month is stored as a string like "Jan", "Feb", etc.
                dob_year = f"{row[6]:04d}"  # Ensure year is four digits
                
                # Insert into Student_detail table (using dob_day, dob_month, dob_year)
                insert_query = """
                INSERT INTO Student_detail (email_id, father_name, address, name, dob_day, dob_month, dob_year, enrol_no, mother_name, mobile_no, 
                                            select_hostel, room_block, room_no)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                
                self.db_cursor.execute(insert_query, (
                    row[0], row[1], row[2], row[3], dob_day, dob_month, dob_year, row[7], row[8], row[9], row[10], row[11], row[12]
                ))
                self.db_connection.commit()  # Commit to the database
                
            messagebox.showinfo("Success", "Student data has been added to Student_detail table")
            # After inserting the data, open the admin_table page
            self.open_admin_table()
        else:
            messagebox.showerror("Error", "No student data found in Registration or Room_book tables")

    def open_admin_table(self):
        # Close the login window before opening the admin table window
        self.root.destroy()  
        
        # Create a new window for the admin table
        admin_root = tk.Tk()
        admin_page = admin_table(admin_root)  # Initialize the admin_table class
        admin_root.mainloop()  # Start the main loop for the admin table page


# In[ ]:


if __name__=='__main__':
    root=tk.Tk()
    obj=Login_Window(root)
    root.mainloop()
    


# In[ ]:




