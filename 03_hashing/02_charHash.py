from typing import List


# main function
def main() -> None:
    # Get input string
    string: str = input()

    # Create hash array for 26 lowercase letters
    hash: List[int] = [0] * 26

    # Count frequency of each character
    # ord(char) - ord('a') maps 'a'->0, 'b'->1, etc.
    for char in string:
        hash[ord(char) - ord("a")] += 1
        # ord() to find the ascii of character

    # Process queries for character frequencies
    queries: int = int(input())
    while queries > 0:
        character: char = input()
        print(
            "The frequency of ",
            character,
            " occured is : ",
            hash[ord(character) - ord("a")],
        )
        queries -= 1


if __name__ == "__main__":
    main()
