from bank import value

def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()

def test_return_zero():
    assert value('hello d') == 0
    assert value('HELLO d') == 0
    assert value('HeLlo d') == 0

def test_return_twenty():
    assert value('hey') == 20
    assert value('HI') == 20

def test_return_hundred():
    assert value('good morning') == 100
    assert value('Good afternoon') == 100

if __name__ == "__main__":
    main()
