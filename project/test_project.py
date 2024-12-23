from project2 import year, make_email
import pytest

def make_email():
    sn = "S190100"
    name = "Harry"
    assert make_email(name, sn) == "s190100harry@harvard.edu"


def year():
    sn = "S190100"
    assert year(sn) == "2019"
