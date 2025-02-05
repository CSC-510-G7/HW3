"""test file for the merge sort functionality in hw2_debugging.py"""
from hw2_debugging import merge_sort

def test_empty_list():
    """tests merge sort on an empty list"""
    expected = []
    assert expected == merge_sort([])

def test_single_item():
    """tests merge sort on a list of length 1"""
    expected = [5]
    assert expected == merge_sort([5])

def test_unsorted_list():
    """tests merge sort on an unsorted list"""
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == merge_sort([7, 5, 6, 1, 2, 4, 3])
