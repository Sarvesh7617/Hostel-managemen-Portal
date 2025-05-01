# CSJMU Hostel Management DBMS Project (Student & Admin Management System)

This project is a **Hostel Database Management System (DBMS)** that allows **students to register, book rooms, and log in**, while **admins can manage student details** using **MySQL database integration & Tkinter-based GUI**.

![image](https://github.com/user-attachments/assets/e5ac7961-7a8b-41dc-b2f9-5c6ef740fa2e)
![image](https://github.com/user-attachments/assets/9d16a24d-0987-49d1-acb3-4744a21a36d8)
![image](https://github.com/user-attachments/assets/97cdfa3d-c560-46ce-8f9c-e80e4e2f94bd)

## Features  
- **Admin Login System** – Admin authentication & student data retrieval  
- **Hostel UI (Main Interface)** – Interactive buttons & contact details  
- **Student Registration Form** – Validation & MySQL storage  
- **Student Login** – Mobile number & DOB-based authentication  
- **Room Booking System** – Hostel & room block selection  
- **Admin Dashboard** – View, update, delete student records  
- **MySQL Database Integration** for structured data storage  


## ⚙️ Technologies Used  
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Database:** MySQL (`mysql.connector`)  
- **Image Processing:** PIL (Python Imaging Library)  
- **Development Environments:** Jupyter Notebook & VS Code  

---

##  Installation  

To run this project locally, **ensure that Jupyter Notebook or VS Code is installed** after cloning the repository.  

1. Clone the Repository**  
```bash
git clone https://github.com/Sarvesh7617/Hostel-managemen-Portal.git
```
2. Navigate to the Project Directory
```bash
cd hostel-dbms
```
3. Install Required Dependencies
```bash
pip install mysql-connector-python pillow
```
## 4. Ensure MySQL Database is Installed & Configured  
To set up the database for this project, follow these steps:  

  1 **Create a database named `management`**  
  2 **Execute the SQL scripts** to set up the following tables:  
   - `Registration`  
   - `Room_book`  
   - `Student_detail`  
## 5: Run the Application in Jupyter Notebook or VS Code  
### **For Jupyter Notebook:**  
```bash
jupyter notebook
```
### **For VS Code:**
```bash
python hostel_ui.py
```
## 📊 Database Schema  

### 🔹 **Student Registration Table**
| **Column**       | **Data Type**  |
|-----------------|--------------|
| `email_id`      | VARCHAR(255) |
| `father_name`   | VARCHAR(255) |
| `address`       | TEXT         |
| `name`         | VARCHAR(255) |
| `dob_day`      | INT          |
| `dob_month`    | VARCHAR(10)  |
| `dob_year`     | INT          |
| `enrol_no`     | VARCHAR(20)  |
| `mother_name`  | VARCHAR(255) |
| `mobile_no`    | VARCHAR(15)  |

### 🔹 **Room Booking Table**
| **Column**       | **Data Type**  |
|-----------------|--------------|
| `select_hostel` | VARCHAR(100) |
| `room_block`    | VARCHAR(50)  |
| `room_no`       | VARCHAR(10)  |

---

## How It Works  

- **Admin logs in** using username-"Dbms project" & password-"Dbms@1234"
- **Student registers** with personal & enrollment details  
- **Student logs in** using mobile number & DOB for verification  
- **System fetches student details** from MySQL database  
- **Admin table displays** all student details for management  
- **Student selects** hostel, room block & room number for booking  
- **Details are stored in MySQL**, and booking confirmation is shown  

---

## Future Enhancements  

- **Implement student search functionality**  
- **Enhance GUI with modern Tkinter styling**  
- **Enable multiple admin roles for better management**  
- **Automate email notifications for booking confirmation**  
