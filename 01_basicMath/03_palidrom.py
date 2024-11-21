from typing import List

# Check if number reads same forwards and backwards
def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    
    original: int = num
    reversed_num: int = 0
    
    # Reverse the number
    while num:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
        
    return original == reversed_num

# Test cases
def main() -> None:
    test_cases: List[int] = [121, -121, 123, 1221, 0]
    for num in test_cases:
        print(f"{num} is{' ' if is_palindrome(num) else ' not '}a palindrome")

if __name__ == "__main__":
    main()