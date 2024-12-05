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
    # Finding the min and max key-value pair
    max_value = max(hashMap.values())
    max_key_pair = max(hashMap.items(), key=lambda x: x[0])
    min_value = min(hashMap.values())
    min_key_pair = min(hashMap.items(), key=lambda x: x[0])
    print(max_key_pair)
    print(min_key_pair)


if __name__ == "__main__":
    main()
