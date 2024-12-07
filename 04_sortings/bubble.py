from typing import List

def bubble_sort(array: List[int]) -> None:
    """
    Sorts the given array using the Bubble Sort algorithm.
    
    Parameters:
    array (List[int]): The list of integers to be sorted.
    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # If no two elements were swapped by inner loop, then the array is already sorted
        if not swapped:
            break

def main() -> None:
    """
    Main function to demonstrate the Bubble Sort algorithm.
    """
    array = [1, 2, 12, 13, 53, 125, 221]
    bubble_sort(array)
    print(array)

if __name__ == '__main__':
    main()
