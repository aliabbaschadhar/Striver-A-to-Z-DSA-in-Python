from typing import List, Dict, Set

def insertionSort(array: List[int]) -> None:
    # Get the size of the array
    size: int = len(array)

    # Iterate through each element in the array
    for i in range(size):
        j: int = i
        # While the current element is greater than the previous one,
        # swap them and move towards the beginning of the array
        while j > 0 and array[j] < array[j-1]:
            # Swap elements
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

# main function
def main() -> None:
    pass
