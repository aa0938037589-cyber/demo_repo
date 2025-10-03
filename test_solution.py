# test_solution.py
import pytest
from solution import two_sum

def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 7) is None

def test_two_sum_multiple_solutions():
    result = two_sum([3, 2, 4], 6)
    assert result in ([1, 2], [2, 1])  # 接受不同索引順序
