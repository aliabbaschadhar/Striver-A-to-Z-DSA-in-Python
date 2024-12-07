from typing import List, Dict, Set

def SelectionSort(array: List[int], size: int) -> None:
    """
    Sorts the given array using the Selection Sort algorithm.
    
    Parameters:
    - array: List[int] - The list of integers to be sorted.
    - size: int - The number of elements in the array.
    """
    # Iterate over each element in the array
    for i in range(0, size - 1):
        # Assume the current element is the minimum
        min_idx: int = i
        
        # Iterate over the unsorted part of the array to find the actual minimum
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the current element
        temp: int = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp


# Main function to demonstrate the SelectionSort algorithm
def main() -> None:
    """
    Main function to initialize an array, print its size, sort it using SelectionSort, and print the sorted array.
    """
    # Initialize an array of integers
    array: List[int] = [1, 25, 2, 11, 22, 34, 5, 21, 5, 21, 52, 552, 512]
    
    # Get the size of the array
    size: int = array.__len__()
    
    # Sort the array using SelectionSort
    SelectionSort(array, size)
    
    # Print the sorted array
    print(array)


if __name__ == '__main__':
    main()
