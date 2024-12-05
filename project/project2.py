import tkinter as tk
from tkinter import filedialog, messagebox
import csv

# Function to handle manual input of student names and numbers
def add_student():
    name = name_entry.get()
    sn = sn_entry.get()
    
    if not name or not sn:
        messagebox.showwarning("Input Error", "Both Name and Student Number are required!")
        return

    # Add to the data list
    data.append({"name": name, "sn": sn})
    name_entry.delete(0, tk.END)
    sn_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"Added {name} ({sn}) successfully!")

# Function to handle CSV file upload
def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "name" in row and "sn" in row:
                    data.append(row)
                else:
                    messagebox.showerror("CSV Error", "Invalid CSV format. Requires 'name' and 'sn' columns.")
                    return
        
        messagebox.showinfo("Success", "CSV file uploaded successfully!")

    except FileNotFoundError:
        messagebox.showerror("File Error", "File not found!")

# Function to generate output CSV
def generate_csv():
    if not data:
        messagebox.showwarning("No Data", "No data to save!")
        return
    
    # Ask for output file location
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "year_joined"])
            writer.writeheader()
            
            for row in data:
                email = make_email(row["name"], row["sn"])
                year_joined = year(row["sn"])
                writer.writerow({"name": row["name"], "email": email, "year_joined": year_joined})
            
            messagebox.showinfo("Success", "CSV file generated successfully!")
    
    except Exception as e:
        messagebox.showerror("File Error", f"Could not write to file: {e}")

# Helper functions
def make_email(name, sn):
    return f"{sn}{name}@harvard.edu".lower()

def year(sn):
    return "20" + sn[1:3]

# GUI setup
root = tk.Tk()
root.title("Student Email Generator")
root.geometry("500x500")

data = []

# Manual Input Section
manual_frame = tk.Frame(root, pady=10)
manual_frame.pack(fill="x")

manual_label = tk.Label(manual_frame, text="Manually Add Students", font=("Arial", 14))
manual_label.pack()

name_label = tk.Label(manual_frame, text="First Name:")
name_label.pack(anchor="w")
name_entry = tk.Entry(manual_frame, width=30)
name_entry.pack()

sn_label = tk.Label(manual_frame, text="Student Number:")
sn_label.pack(anchor="w")
sn_entry = tk.Entry(manual_frame, width=30)
sn_entry.pack()

add_button = tk.Button(manual_frame, text="Add Student", command=add_student)
add_button.pack(pady=10)

# File Upload Section
file_frame = tk.Frame(root, pady=10)
file_frame.pack(fill="x")

file_label = tk.Label(file_frame, text="Upload CSV File", font=("Arial", 14))
file_label.pack()

upload_button = tk.Button(file_frame, text="Upload CSV", command=upload_csv)
upload_button.pack(pady=10)

# Generate CSV Section
generate_frame = tk.Frame(root, pady=20)
generate_frame.pack(fill="x")

generate_button = tk.Button(generate_frame, text="Generate CSV", command=generate_csv, bg="green", fg="white")
generate_button.pack()

# Run the application
root.mainloop()
