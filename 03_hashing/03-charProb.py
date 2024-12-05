# Using hash map to store and query character frequencies
from typing import Dict

# main function
def main() -> None:
    string: str = input()
    # Store character frequencies in map
    hashMap: Dict[str, int] = {}
    for char in string:
        # Using setdefault to handle both new and existing char in hashMap if char exists then add one to it's previous value if not then set it to and add one to it
        hashMap[char] = hashMap.setdefault(char, 0) + 1

    # Process queries for character counts
    quries: int = int(input())
    while quries > 0:
        # Take only first character from input using [0]
        letter: str = input().strip()[0]
        # Using get to safely handle characters that might not exist in string
        count: int = hashMap.get(letter, 0)
        print(letter, " has occurred ", count, "times")
        quries -= 1


if __name__ == "__main__":
    main()
