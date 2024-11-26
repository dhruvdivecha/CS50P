from numb3rs import validate

def main():
    test_range()
    test_format()

def test_range():
    assert validate(r"100.20.23.45") == True
    assert validate(r"275.20.23.45") == False
    assert validate(r"100.300.23.45") == False

def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"cat") == False

if __name__ == "__main__":
    main()
