
Video URL:

-----------------------------------------------------------------------------------------------------------------------------------------------------------


# README

## **Student Email Generation Program**

### **Overview**
This Python script is a utility tool designed to automate the creation of customised student email addresses based on their student numbers and first names. The program processes data stored in a CSV file, extracts necessary information, and generates email addresses in a standard format. Additionally, it derives the year the student joined based on their student number. The output is saved as a new CSV file, making it ready for further use or integration into school systems.

Name: Dhruv Hitesh Divecha

Github username: dhruvdivecha
edX username: dhruvdivecha

City, country: Dar Es Salaam, Tanzania

Date: 26th November 2024

---

### **How It Works**

1. **Input CSV File**
   The program takes an input CSV file that contains two columns:
   - `name`: The student's first name.
   - `sn`: The student number, which uniquely identifies each student.

   Example:
   ```csv
   name,sn
   John,20213456
   Alice,20182345
   ```

2. **Email Generation**
   Each student's email address is generated in the format:
   `student_number + first_name + "@harvard.edu"`.
   For example, for a student with the name "John" and student number "S213456", the email would be:
   `s213456john@harvard.edu`.

   All email addresses are converted to lowercase for consistency.

3. **Year Joined Extraction**
   The first two digits after the leading digit in the student number (`sn`) are used to calculate the year the student joined. For example:
   - For `sn = S213456`, the year is derived as `20 + 21 = 2021`.
   - For `sn = S182345`, the year is `20 + 18 = 2018`.

4. **Output CSV File**
   The program generates a new CSV file containing three columns:
   - `name`: The student's name.
   - `email`: The customised email address.
   - `year_joined`: The year the student joined.

   Example:
   ```csv
   name,email,year_joined
   John,s213456john@harvard.edu,2021
   Alice,s182345alice@harvard.edu,2018
   ```

---

### **Usage**

#### **Command-Line Arguments**
The script requires two command-line arguments:
1. The input CSV file (e.g., `students.csv`).
2. The output CSV file (e.g., `emails.csv`).

**Syntax:**
```bash
python script.py input.csv output.csv
```

#### **Error Handling**
The script is robust and includes error-handling mechanisms for common issues:
1. **Missing Arguments**: If fewer than two arguments are provided, the script terminates with a "Too few command-line arguments" error.
2. **Extra Arguments**: If more than two arguments are given, the script terminates with a "Too many command-line arguments" error.
3. **Incorrect File Type**: If the provided files are not in CSV format, the script terminates with a "Not a csv file" error.
4. **File Not Found**: If the input file is not found, the script terminates with an "Incorrect csv" error.

---

### **Functions**

1. **`main()`**
   - The core function that coordinates the overall workflow.
   - Reads data from the input file, processes it, and writes results to the output file.

2. **`check_args()`**
   - Validates the command-line arguments to ensure the correct number and file types.

3. **`make_email(name, sn)`**
   - Generates a lowercase email address by concatenating the student number, name, and the domain `"@harvard.edu"`.

4. **`year(sn)`**
   - Extracts the year of joining from the student number.

---

### **Dependencies**
The script relies on Python's built-in libraries:
- `sys`: For command-line argument handling.
- `csv`: For reading and writing CSV files.

No additional libraries are required.

---

### **Example Workflow**

1. Input File (`students.csv`):
   ```csv
   name,sn
   John,S213456
   Alice,S182345
   ```

2. Running the Script:
   ```bash
   python script.py students.csv emails.csv
   ```

3. Output File (`emails.csv`):
   ```csv
   name,email,year_joined
   John,s213456john@harvard.edu,2021
   Alice,s182345alice@harvard.edu,2018
   ```

---

### **Customisation**
This script can be adapted to:
- Change the email domain (e.g., from `"@harvard.edu"` to another domain).
- Incorporate additional columns, such as last names or departments.

---

### **Conclusion**
This program provides an efficient and scalable solution for generating customised email addresses and associated metadata. Its intuitive design, error handling, and reliance on built-in libraries make it ideal for use in educational institutions.

