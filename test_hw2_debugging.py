import pytest
from hw2_debugging import merge_sort

# Test 1: Merge Sort should correctly sort an already sorted array
def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test 2: Merge Sort should correctly sort a reverse-sorted array
def test_merge_sort_reverse():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# Test 3: Merge Sort should correctly sort a randomly ordered array
def test_merge_sort_unsorted():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]

