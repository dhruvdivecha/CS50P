from project import year, check_args, make_email
import pytest

def check_args():
    with pytest.raises(SystemExit):
        check_args()


def make_email():
    sn = S190100
    name = Harry
    assert make_email(name, sn) == "S190100Harry@harvard.edu"


def year():
    sn = S190100
    assert year(sn) == "2019"
