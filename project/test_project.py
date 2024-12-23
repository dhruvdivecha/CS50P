import pytest
from project2 import make_email, year

def test_make_email():
    assert make_email("JohnDoe", "S123456") == "s123456johndoe@harvard.edu"
    assert make_email("JaneSmith", "S654321") == "s654321janesmith@harvard.edu"

def test_year():
    assert year("S123456") == "2012"
    assert year("S654321") == "2065"
    
if __name__ == "__main__":
    test_make_email()
    test_year()
   

