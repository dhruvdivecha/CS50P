import os
import csv
from test_project import make_email, year, add_student, upload_csv, generate_csv

def test_make_email():
    assert make_email("JohnDoe", "123456") == "123456johndoe@harvard.edu", "Email generation failed"
    assert make_email("JaneSmith", "654321") == "654321janesmith@harvard.edu", "Email generation failed"

def test_year():
    assert year("123456") == "2012", "Year extraction failed"
    assert year("654321") == "2054", "Year extraction failed"

def test_add_student():
    data = []
    name = "Test Student"
    sn = "101001"
    add_student(name, sn, data)
    assert len(data) == 1, "Failed to add student to data"
    assert data[0]["name"] == "Test Student", "Name mismatch"
    assert data[0]["sn"] == "101001", "Student number mismatch"

def test_upload_csv():
    test_csv_path = "test_upload.csv"
    data = []

    with open(test_csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "sn"])
        writer.writeheader()
        writer.writerow({"name": "JohnDoe", "sn": "202345"})

    upload_csv(test_csv_path, data)

    assert len(data) == 1, "CSV upload failed"
    assert data[0]["name"] == "JohnDoe", "Uploaded name mismatch"
    assert data[0]["sn"] == "202345", "Uploaded student number mismatch"

    os.remove(test_csv_path)

def test_generate_csv():
    test_output_path = "test_output.csv"
    data = [
        {"name": "Alice", "sn": "301234"},
        {"name": "Bob", "sn": "401567"}
    ]

    generate_csv(test_output_path, data)

    assert os.path.exists(test_output_path), "CSV generation failed"

    with open(test_output_path, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 2, "CSV row count mismatch"
        assert rows[0]["name"] == "Alice", "First row name mismatch"
        assert rows[0]["email"] == "301234alice@harvard.edu", "First row email mismatch"
        assert rows[0]["year_joined"] == "2030", "First row year mismatch"

    os.remove(test_output_path)

if __name__ == "__main__":
    test_make_email()
    test_year()
    test_add_student()
    test_upload_csv()
    test_generate_csv()

    print("All tests passed!")
