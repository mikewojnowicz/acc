import pytest  # noqa

from acc.arithmetic import  add_numbers_incorrectly

def test_add_numbers_incorrectly():
    assert add_numbers_incorrectly(2,0)==2
    assert add_numbers_incorrectly(2,1)==3

