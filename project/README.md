
Video URL:

-----------------------------------------------------------------------------------------------------------------------------------------------------------



# **Student Email Generator GUI**

Name: Dhruv Hitesh Divecha

Github username: dhruvdivecha
edX username: dhruvdivecha

City, country: Dar Es Salaam, Tanzania

Date: 26th November 2024

---
This project provides a graphical user interface (GUI) application for generating custom student email addresses and determining their joining year based on their student number. Users can either manually input student data or upload a CSV file containing the data, and the program generates a new CSV file with the required information.



## **Features**

1. **Manual Data Input**  
   - Users can enter the **first name** and **student number** of students through the GUI.
   - Added data is stored in memory until the user generates the final CSV file.

2. **CSV File Upload**  
   - Allows uploading of a CSV file containing student data.
   - The input file must have the following columns:  
     - `name` (First Name)  
     - `sn` (Student Number)  

3. **Generate Output CSV**  
   - Combines manually entered data and uploaded CSV data.
   - Generates a CSV file with the following columns:  
     - `name`: Student's first name.  
     - `email`: A custom email in the format `{student_number}{name}@harvard.edu`.  
     - `year_joined`: The year derived from the first two digits of the student number (e.g., `23 → 2023`).  

4. **User-Friendly Interface**  
   - Built with `tkinter` for ease of use.
   - Clear error messages and feedback for invalid actions.

---

## **How to Use**

### **1. Run the Program**
Ensure you have Python 3.x installed. Then, run the script:
```bash
python script_name.py
```
Replace `script_name.py` with the name of the Python file.

---

### **2. Input Methods**

#### **Manual Data Entry**
- In the "Manually Add Students" section:
  - Enter the **first name** and **student number**.
  - Click the **Add Student** button to add the data.
  - Repeat for additional students.

#### **CSV File Upload**
- In the "Upload CSV File" section:
  - Click the **Upload CSV** button.
  - Select a valid CSV file with the required columns:
    - `name`: First Name.  
    - `sn`: Student Number.  

---

### **3. Generate CSV File**
- Once all desired data is added (manually or via file upload):
  - Click the **Generate CSV** button in the "Generate CSV File" section.
  - Choose a location to save the output file.
  - The generated CSV will include:
    - `name`: First name.  
    - `email`: Custom email in the format `{student_number}{name}@harvard.edu`.  
    - `year_joined`: The joining year derived from the student number.

---

## **Input Requirements**

### **Manual Input**
- **Name**: Only the student's first name (letters only, no spaces or special characters).
- **Student Number**: A numeric identifier, e.g., `S2301`.

### **CSV File Format**
The input CSV file must include the following columns:
- `name`: The student's first name.
- `sn`: The student's number.

Example CSV File:
```csv
name,sn
John,S2301
Jane,S2402
```

---

## **Output CSV**
The generated CSV file includes:
- `name`: Student's first name.
- `email`: Custom email in the format `{student_number}{name}@harvard.edu`.
- `year_joined`: The year the student joined, derived from the first two digits of the student number.

Example Output:
```csv
name,email,year_joined
John,2301john@harvard.edu,2023
Jane,2402jane@harvard.edu,2024
```

---

## **Error Handling**

1. **Manual Input Errors**  
   - Both fields (**name** and **student number**) must be filled.  
   - An error message is displayed if either field is empty.

2. **CSV File Errors**  
   - The uploaded file must be a valid CSV with `name` and `sn` columns.  
   - If the file is invalid, an error message is displayed.

3. **No Data to Save**  
   - An error is displayed if the user attempts to generate the CSV without any data.

4. **File Writing Errors**  
   - If the program encounters an error while writing the output file, a detailed error message is displayed.

---

## **Code Overview**

### **1. Functions**
- `add_student`: Adds manually entered student data to the internal list.  
- `upload_csv`: Processes an uploaded CSV file and appends its data to the internal list.  
- `generate_csv`: Generates the output CSV file with `name`, `email`, and `year_joined` columns.  
- `make_email`: Generates an email using the format `{student_number}{name}@harvard.edu`.  
- `year`: Extracts the joining year from the first two digits of the student number.

### **2. GUI Structure**
- **Manual Input Section**: Fields to enter the student's name and student number, along with a button to add data.  
- **File Upload Section**: Button to upload a CSV file containing student data.  
- **Generate CSV Section**: Button to generate and save the final output CSV file.  

---

## **Future Enhancements**

1. Add validation for student numbers to ensure a consistent format.  
2. Include additional columns such as last name or department.  
3. Add preview functionality to view the entered or uploaded data before generating the output.  
4. Improve error messages with more detailed guidance.  

---

## **Credits**
This project uses Python's built-in libraries:  
- `tkinter` for GUI development.  
- `csv` for handling CSV files.  
- `filedialog` and `messagebox` for file selection and error notifications.  

--- 

Enjoy using the **Student Email Generator GUI**! 😊