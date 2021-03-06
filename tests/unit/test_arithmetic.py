import random

import pytest

from acc.arithmetic import add_numbers_incorrectly


def test__add_numbers_incorrectly__adding_something_plus_zero():
    assert add_numbers_incorrectly(2, 0) == 2


def test__add_numbers_incorrectly__adding_something_plus_one():
    assert add_numbers_incorrectly(2, 1) == 3


@pytest.mark.skip("Saving this for later")
def test__add_numbers_incorrectly__with_random_numbers():
    random.seed(1)
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    expected_result = x + y
    assert add_numbers_incorrectly(x, y) == expected_result
