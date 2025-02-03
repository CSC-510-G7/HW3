"""This module contains an implementation of bubble sort"""
import rand

def bubble_sort(arr: list[int]):
    """
    Bubble sort implemenation

    Args:
        arr: list of ints
    """

    # special case: length 0, 1
    if len(arr) < 2:
        return arr

    # repeat until array is sorted
    done = False
    while not done:
        done = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                # swap if right < left
                done = False
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp

    return arr

test_arr = rand.random_array([None] * 20)
arr_out = bubble_sort(test_arr)

print(arr_out)
