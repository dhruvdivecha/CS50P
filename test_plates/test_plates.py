from plates import is_valid

def main():
    test_min_max()
    test_2_letters()
    test_no_num()
    test_punctuation()

def test_min_max():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False

def test_2_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False

def test_no_num():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('.?,!@#*') == False
    assert is_valid('AA@AAA') == False
