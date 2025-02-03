# import subprocess

# def random_array(arr):
#     shuffled_num = None
#     for i in range(len(arr)):
#         shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
#         arr[i] = int(shuffled_num.stdout)
#     return arr

"""
This module's fix was written by my groupmate Kanchana (kds)
"""

import secrets

def random_array(arr):
    """Generates a random array with values between 1 and 20."""
    for idx, _ in enumerate(arr):
        arr[idx] = secrets.randbelow(21)  # Replaced subprocess with secrets.randbelow() to pass bandit security
    return arr
