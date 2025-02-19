"""This module contains an implementation of mergesort"""
import rand


def merge_sort(arr):
    """
    This method splits up the array for mergesort
    Args:
        arr: list to be sorted
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """
    This method recombines the arrays for mergesort

    Args:
        left_arr: left half of list
        right_arr: right half of list
    """
    left_index = 0
    right_index = 0
    merge_arr = []
    merge_idx = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1
        merge_idx += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr

test_arr = rand.random_array([None] * 20)
arr_out = merge_sort(test_arr)

print(arr_out)
