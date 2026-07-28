"""
test_prime.py — Unit tests for the is_prime function in prime_checker.py

Run this file to automatically verify that prime_checker works correctly.
"""

from prime_checker import is_prime


def run_tests():
    """Run a series of test cases and print results."""
    test_cases = [
        # (number, expected_result)
        (1, False),    # 1 is NOT prime
        (2, True),     # 2 IS prime
        (3, True),     # 3 IS prime
        (4, False),    # 4 is NOT prime
        (5, True),     # 5 IS prime
        (7, True),     # 7 IS prime
        (10, False),   # 10 is NOT prime
        (13, True),    # 13 IS prime
        (17, True),    # 17 IS prime
        (20, False),   # 20 is NOT prime
        (25, False),   # 25 is NOT prime
        (29, True),    # 29 IS prime
        (97, True),    # 97 IS prime
        (100, False),  # 100 is NOT prime
        (0, False),    # 0 is NOT prime
        (-7, False),   # Negative numbers are NOT prime
    ]

    passed = 0
    failed = 0

    for number, expected in test_cases:
        result = is_prime(number)
        if result == expected:
            print(f"  ✔ is_prime({number}) = {result}  (expected {expected})")
            passed += 1
        else:
            print(f"  ✘ is_prime({number}) = {result}  (expected {expected}) — FAILED")
            failed += 1

    print("\n" + "=" * 40)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    if failed == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed.")


if __name__ == "__main__":
    run_tests()
