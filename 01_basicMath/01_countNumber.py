from math import log10

def numberOfDigits(number):
    # count = 0
    # while number > 0:
    #     # / is used for floating point numbers and using this the digit will not gonna become zero like78893/10 = 7989.3 ... 7.989 which is still > 0
    #     # "//" is used for integer division
    #     number = number // 10
    #     count += 1
    # return count
    cnt = int(log10(number)+1)
    return cnt;


def main():
    number = 79893
    print(f"Number of digits in {number} is: {numberOfDigits(number)}")

if __name__ == "__main__":
    main()