"""This module includes a prime number checker"""

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
