import types


def oneToN_Times(num: int, i: int) -> None:
    if i > num:
        return
    print(i)
    return oneToN_Times(
        num, i + 1
    )  # Returning the function with some changed parameters


# N to one
def NtoOne(num: int) -> None:
    if num <= 0:
        return
    print(num)
    return NtoOne(num - 1)


# Some of first n number
def sumOf(num: int) -> int:
    sum: int = 0
    if num < 0:
        return 0
    return num + sumOf(num - 1)


# factorial
def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


# fibnocci
def fibnocci(num: int) -> int:
    if num == 1 or num == 0:
        return 1
    return fibnocci(num - 1) + fibnocci(num - 2)


# Reverse an array
def reverse(arr: list, i, n) -> list:
    if i > arr.__len__() // 2:
        return arr
    arr[i], arr[n - 1] = arr[n - 1], arr[i]
    return reverse(arr, i + 1, n - 1)


# Checking a string is a palindrom
def isPalindrom(string: str, i: int) -> bool:
    if i > string.__len__() // 2:
        return True
    if string[i] != string[string.__len__() - i - 1]:
        return False
    return isPalindrom(string, i + 1)


# main function
def main() -> None:
    num: int = 6
    # oneToN_Times(num,1)
    # NtoOne(num)
    # print(sumOf(num))
    # print(factorial(num))
    # print(fibnocci(num))
    arr: list = [1, 2, 3, 4, 5]
    # print(reverse(arr,0,arr.__len__()))
    string: str = "madam"
    print(isPalindrom(string, 0))


if __name__ == "__main__":
    main()
