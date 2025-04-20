import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import mysql.connector

class studentLogin:
    def __init__(self, root):
        self.root = root
        self.root.title('Hostel Room Management System')
        self.root.geometry("1050x365+230+315")     

        # =============================== Create variables ===============#
        self.mobile = tk.StringVar()
        self.day = tk.StringVar()
        self.month = tk.StringVar()
        self.year = tk.StringVar()
        self.student_mobile = None

        # ======================== Title ============================#
        login_title = tk.Label(self.root, text="Student Login for Hostel", font=("Times New Roman", 20, "bold"), fg="deep sky blue")
        login_title.place(x=-130, y=0, width=1295)

        # ======================= Form ============================#
        label_number = tk.Label(self.root, text="Your Mobile No :", font=("Times New Roman", 15), bg=None)
        label_number.place(x=100, y=100)
        
        entry_number = tk.Entry(self.root, textvariable=self.mobile, width=20, font=('Times', 15), highlightbackground="blue", highlightcolor="green")
        entry_number.place(x=260, y=102)
        
        label_dob = tk.Label(self.root, text="Enter DOB:", font=("Times New Roman", 15))
        label_dob.place(x=102, y=150)
        
        # Combobox for Day (1-31)
        combo_day = ttk.Combobox(self.root, textvariable=self.day, width=5, font=('Times', 15), state='readonly')
        combo_day['value'] = ['Day'] + [int(i) for i in range(1, 32)]
        combo_day.current(0)
        combo_day.place(x=260, y=150)
        
        # Label for '-'
        label_dash1 = tk.Label(self.root, text="-", font=("Times New Roman", 15))
        label_dash1.place(x=335, y=150)
        
        # Combobox for Month (1-12)
        combo_month = ttk.Combobox(self.root, textvariable=self.month, width=10, font=('Times', 15), state='readonly')
        combo_month['value'] = ['Month'] + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        combo_month.current(0)
        combo_month.place(x=350, y=150)
        
        # Label for '-'
        label_dash2 = tk.Label(self.root, text="-", font=("Times New Roman", 15))
        label_dash2.place(x=475, y=150)
        
        # Combobox for Year (e.g., 1900-2024)
        combo_year = ttk.Combobox(self.root, textvariable=self.year, width=8, font=('Times', 15), state='readonly')
        combo_year['value'] = ['Year'] + [int(i) for i in range(1980, 2025)]
        combo_year.current(0)
        combo_year.place(x=490, y=150)

        # ============================= Submit Button ==============================#
        login_btn = tk.Button(self.root, command=self.Login_form, text="Login", width=10, font=("Times New Roman", 13, "bold"), bg="red", fg="white", bd=0, cursor="hand1")
        login_btn.place(x=270, y=200)

        # ================================== Main Frame ==================#
        contact_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE)
        contact_frame.place(x=100, y=260, width=450, height=100)

        # ========================== Contact ============================#   
        contact_boys = tk.Label(contact_frame, text="Helpdesk Boys hostel: +91-XXXXXXX542 ( Mr Anuraag )", font=("Times New Roman", 12), fg="deep pink")
        contact_boys.place(x=0, y=0)
        
        contact_girls = tk.Label(contact_frame, text="Helpdesk Girls hostel: +91-XXXXXXX345 (Mrs. Rita Kushwaha)", font=("Times New Roman", 12), fg="deep pink")
        contact_girls.place(x=0, y=30)
        
        contact_more = tk.Label(contact_frame, text="For all other queries: +91-XXXXXXX342 (Mr Saurabh Madi Tripathi)", font=("Times New Roman", 12), fg="deep pink")
        contact_more.place(x=0, y=60)

    # =============================== Helper Functions =========================#
    def get_number(self):
        return self.mobile.get()

    def fetch_student_details(self, mobile_number, day, month, year):
        conn = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="Kashish@1234",
            database="management"
        )
        my_cursor = conn.cursor()

        query = """
        SELECT mobile_no
        FROM Registration 
        WHERE mobile_no=%s AND dob_day=%s AND dob_month=%s AND dob_year=%s
        """
        value = (mobile_number, day, month, year)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        conn.close()

        return row  # Return the fetched data

    # =============================== Login Form =============================#
    def Login_form(self):
        mobile_number = self.mobile.get().strip()
        day = self.day.get()
        month = self.month.get()
        year = self.year.get()

        # Validate the mobile number and DOB fields
        if mobile_number == '':
            messagebox.showerror("Error", "Please enter Contact number", parent=self.root)
        elif len(mobile_number) != 10:
            messagebox.showerror("Error", "Mobile number must be 10 digits", parent=self.root)
        elif not mobile_number.isdigit():
            messagebox.showerror("Error", "Mobile number must contain only digits", parent=self.root)
        elif day == 'Day' and month == 'Month' and year == 'Year':
            messagebox.showerror("Error", "Please enter Day, Month, Year", parent=self.root)
        else: 
            self.student_mobile = mobile_number  # Store the mobile number

            # Fetch student details (from the database)
            row = self.fetch_student_details(mobile_number, day, month, year)

            if row is None:
                messagebox.showerror("Error", "You are not a registered student. Please register first.", parent=self.root)
            else:
                # Directly open the Book Hostel page (pass student name and mobile)
                self.Book(mobile_number)

    def Book(self,student_mobile):
        # Open new window for room booking
        self.new_window = tk.Toplevel(self.root)
        
        # Pass the new window, student name, and mobile number
        bookHostel(self.new_window,student_mobile)

class bookHostel:
    def __init__(self, root,student_mobile):
        self.root = root
        self.student_mobile = student_mobile  # Store the student's mobile
        self.root.title('Book Hostel')
        self.root.geometry("1050x365+230+315")  # Set window size

        # Create labels and comboboxes (for hostel, room block, etc.)
        self.room_block = tk.StringVar()
        self.room_no = tk.StringVar()
        self.hostel_name = tk.StringVar()

        book_title = tk.Label(self.root, text="Hostel Booking Form", font=("Times New Roman", 20, "bold"), fg="blue")
        book_title.place(x=450, y=0,width=310)
        
        hostel_label = tk.Label(self.root, text="Hostel Name:", font=("Times New Roman", 15))
        hostel_label.place(x=100, y=60)
        hostel_combobox = ttk.Combobox(self.root, textvariable=self.hostel_name, font=("Times New Roman", 15), width=20,state='readonly')
        hostel_combobox['values'] = ["Select Hostel", "Boys Hostel", "Girls Hostel"]
        hostel_combobox.current(0)
        hostel_combobox.place(x=200, y=60)

        room_block_label = tk.Label(self.root, text="Room Block:", font=("Times New Roman", 15))
        room_block_label.place(x=50, y=100)
        room_block_combobox = ttk.Combobox(self.root, textvariable=self.room_block, font=("Times New Roman", 15), width=20,state='readonly')
        room_block_combobox['values'] =["Select Block"]+["A", "B", "C","D"]  # Using single characters for room block
        room_block_combobox.current(0)
        room_block_combobox.place(x=200, y=100)

        room_no_label = tk.Label(self.root, text="Room Number:", font=("Times New Roman", 15))
        room_no_label.place(x=50, y=140)
        room_no_combobox = ttk.Combobox(self.root, textvariable=self.room_no, font=("Times New Roman", 15), width=20,state='readonly')
        room_no_combobox['values'] = ['Room No'] + [int(i) for i in range(1, 51)]
        room_no_combobox.current(0)
        room_no_combobox.place(x=200, y=140)

        submit_button = tk.Button(self.root, text="Submit", font=("Times New Roman", 15), bg="red",command=self.submit_action,cursor="hand1")
        submit_button.place(x=200, y=200)

    def submit_action(self):
        # Check if fields are selected, else show an error message
        if self.hostel_name.get() == "Select Hostel" or self.room_block.get() == "Select Block" or self.room_no.get() == "Select Room":
            messagebox.showerror("Error", "Please select all fields to book the room.", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Kashish@1234",
                    database="management"
                )
                my_cursor = conn.cursor()

                # Insert the room booking details into the Room_book table
                my_cursor.execute("""
                    INSERT INTO Room_book (mobile_no, select_hostel, room_block, room_no)
                    VALUES (%s, %s, %s, %s)
                """, (
                    int(self.student_mobile),  # Convert mobile to INT as per table schema
                    self.hostel_name.get(),
                    self.room_block.get(),
                    int(self.room_no.get())  # Room number is an INT
                ))

                # Commit the transaction to save the data in the database
                conn.commit()

                # Close the database connection
                conn.close()

                # Show success message
                messagebox.showinfo("Success", f"Room {self.room_no.get()} booked successfully in {self.room_block.get()} at {self.hostel_name.get()}", parent=self.root)

                # Close the current booking window
                self.root.destroy()  # This closes the 'bookHostel' window

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error occurred: {err}", parent=self.root)

# Main execution of studentLogin
if __name__ == '__main__':
    root = tk.Tk()
    obj = studentLogin(root)
    root.mainloop()


# In[13]:





# In[ ]:




