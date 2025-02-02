"""
This module generates a random array using Python's built-in random module.
"""

import random

def random_array(arr):
    """Generates a random array with values between 1 and 20."""
    for i in range(len(arr)):
        arr[i] = random.randint(1, 20)  # Replaced subprocess with random.randint()
    return arr
