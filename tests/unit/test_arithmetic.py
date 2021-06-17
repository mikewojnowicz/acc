import pytest  # noqa
import random 

from acc.arithmetic import  add_numbers_incorrectly

def test_add_numbers_incorrectly():
    assert add_numbers_incorrectly(2,0)==2
    assert add_numbers_incorrectly(2,1)==3

def test_add_numbers_incorrectly_with_random_numbers():
    random.seed()
    x=random.uniform(0, 1)
    y=random.uniform(0, 1)
    expected_result = x+y 
    assert add_numbers_incorrectly(x,y)==expected_result 