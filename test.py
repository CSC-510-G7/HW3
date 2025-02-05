"""Tests for the hw2_debugging.py mergesort implementation"""

from hw2_debugging import merge_sort

def test_empty():
    """Test sorting an empty list"""
    assert merge_sort([]) == []

def test_sorted():
    """Test sorting a sorted list"""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unsorted():
    """Test sorting a reverse sorted list"""
    assert merge_sort([3, 2, 5, 1, 4]) == [1, 2, 3, 4, 5]
