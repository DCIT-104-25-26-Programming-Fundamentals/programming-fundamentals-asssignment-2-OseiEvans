# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def is_prime(number):
    """
    Check if a given number is prime.

    A prime number is a whole number greater than 1 that has no divisors
    other than 1 and itself.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Numbers less than 2 are NOT prime
    if number < 2:
        return False

    # Check divisors from 2 up to the square root of the number
    # If any divisor divides evenly, the number is NOT prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    # If no divisors found, the number is prime
    return True


# =============================================================================
# MAIN BLOCK
# =============================================================================

if __name__ == "__main__":
    # Get input from the user
    user_input = int(input("Enter a number: "))

    # Call the function to check if the number is prime
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")

