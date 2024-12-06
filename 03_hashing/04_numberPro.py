# Count frequencies of numbers using hashmap
from typing import Dict, List


# main function
def main() -> None:
    # Convert space separated input into list of integers
    # array: List[int] = list(map(int, input().strip().split()))
    array: List[int] = [1, 2, 3, 4, 5, 5, 5, 6, 4, 2, 21, 1, 2, 1, 1]
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
    max_key_value_ACCToValue = max(hashMap.items(),key=lambda values: values[1])# According to the value 
    min_key_value_ACCToValue = min(hashMap.items(),key=lambda values: values[1])
    max_key_pair = max(
        hashMap.items(), key=lambda x: x[0]
    )  # finding max according to key not the value like{{1,13},{2,3}} --> {2,3}
    min_key_pair = min(hashMap.items(), key=lambda x: x[0])
    print("-----**According to value**------ ")
    print(max_key_value_ACCToValue)
    print(min_key_value_ACCToValue)
    print("-----**According to key**------ ")
    print(max_key_pair)
    print(min_key_pair)


if __name__ == "__main__":
    main()
