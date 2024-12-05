# Count frequencies of numbers using hashmap
from typing import Dict, List


# main function
def main() -> None:
    # Convert space separated input into list of integers
    array: List[int] = list(map(int, input().strip().split()))
    # Store frequencies in hashmap: number -> count
    hashMap: Dict[int, int] = {}
    for num in array:
        hashMap[num] = hashMap.setdefault(num, 0) + 1
    
    # Handle queries to find frequency of numbers
    queries: int = int(input())
    while queries > 0:
        number: int = int(input())
        count: int = hashMap.get(number, 0)
        print(number, " has occured ", count, "times")
        queries -= 1


if __name__ == "__main__":
    main()
