from seasons import Validity
import pytest

def main():
    test_Validity()

def test_Validity():
    assert Validity('July 18,1999') == None
    assert Validity('2006-03-23') == ("2006", "03", "23")
    assert Validity('1998-3-3') == None


if __name__ == "__main__":
    main()
