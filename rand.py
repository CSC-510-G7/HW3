"""This module provides a function to generate a random array of integers."""

import subprocess

def random_array(length):
    """Generates a random array of integers."""
    arr = []
    for _ in range(length):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr.append(int(shuffled_num.stdout))
    return arr
