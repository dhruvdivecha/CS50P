from twttr import shorten

def main():
    test()
    test_no()
    test_pun()

def test():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_no():
    assert shorten('1234') == '1234'

def test_pun():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()

