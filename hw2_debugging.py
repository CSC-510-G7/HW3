"""
This module contains an implementation of Merge Sort and a faulty prime number checker.
"""

import rand

def merge_sort(arr):
    """Performs Merge Sort on the given list."""
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left_sorted = merge_sort(arr[:half])
    right_sorted = merge_sort(arr[half:])

    return recombine(left_sorted, right_sorted)

def recombine(left_arr, right_arr):
    """Merges two sorted lists into one sorted list."""
    left_index = 0
    right_index = 0
    merged_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    merged_arr.extend(left_arr[left_index:])
    merged_arr.extend(right_arr[right_index:])

    return merged_arr

# Faulty Code for step3 (Prime Number Checker)
def faulty_is_prime(n):
    """Checks if a number is prime (contains logical errors)."""
    if n <= 1:  # Fixed: 1 and negatives are NOT prime
        return False  

    for i in range(2, int(n ** 0.5) + 1):  # Fixed: Only check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Test the faulty function
print("Is 1 prime?", faulty_is_prime(1))  # Expected: False
print("Is 9 prime?", faulty_is_prime(9))  # Expected: False
print("Is 17 prime?", faulty_is_prime(17))  # Expected: True

# Generating and sorting a random array
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
