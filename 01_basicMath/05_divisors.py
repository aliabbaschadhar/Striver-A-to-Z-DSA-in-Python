from typing import List 
from math import sqrt

# Brute force approach to find all divisors
# Time Complexity: O(n) where n is the input number
def find_divisors_brute_force(number: int) -> None:
    divisor_list: list = []
    # Check all numbers from 1 to number
    for potential_divisor in range(1, number + 1):
        if number % potential_divisor == 0:    # If it divides number evenly, it's a divisor
            divisor_list.append(potential_divisor)
    # Print all divisors with space between them
    for divisor in divisor_list:
        print(divisor, end=" ")
    
# Optimal solution using square root method
# Time Complexity: O(sqrt(n)) where n is the input number
def find_divisors_optimal(number: int) -> list:
    divisor_list: list = []
    # We only need to check up to square root of number
    square_root: int = int(sqrt(number))
    
    # Check numbers from 1 to square root
    for potential_divisor in range(1, square_root + 1):
        if number % potential_divisor == 0:    # If it's a divisor
            divisor_list.append(potential_divisor)    # Add the smaller divisor
            # If potential_divisor² != number, then number/potential_divisor is also a divisor
            corresponding_divisor = number // potential_divisor
            if potential_divisor != corresponding_divisor:
                divisor_list.append(corresponding_divisor)    # Add the larger divisor
    
    return sorted(divisor_list)

def main()->None:
    # Test with number 36
    test_number: int = 36
    # Get all divisors using optimal method
    all_divisors = find_divisors_optimal(test_number)
    # Print each divisor
    for divisor in all_divisors:
        print(divisor)

if __name__ == "__main__":
    main()