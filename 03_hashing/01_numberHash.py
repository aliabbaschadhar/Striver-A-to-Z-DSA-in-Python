from typing import List
from functools import reduce


# Count occurrences of a number in array
def count(arr: List[int], num: int) -> int:
    noOf: int = 0
    for i in range(len(arr)):
        if num == i:
            noOf += 1
    return noOf


# main function
def main() -> None:
    # arr: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # newArr = list(filter(lambda x: x % 2 == 0, arr))
    # newArr = list(map(lambda x: x * x, newArr))
    # newArr = reduce(lambda x, y: x + y, newArr)

    arr: List[int] = list(
        map(int, input().strip().split())
    )  # To get input from input.txt as a complete list
    # int() it is a function , strip() removes the widespaces , split() create a list of string

    # Create hash array
    size: int = max(arr) + 1
    hash: List[int] = [0] * size  # initializing whole list with zero

    # Count frequencies
    for num in arr:
        hash[num] += 1

    # Process queries
    queries: int = int(input())
    while (queries) > 0:
        number: int = int(input())
        print(hash[number])
        queries -= 1


if __name__ == "__main__":
    main()
