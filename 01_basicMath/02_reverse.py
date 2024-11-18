
#program
def reverseNumber(number:int)->int:
    reverseNum:int = 0
    #For negative number
    is_negative:bool = number<0
    number = abs(number) #Making -ve into absolute number/positive number
    while(number>0):
        lastDigit:int = number%10
        reverseNum = (reverseNum*10)+lastDigit
        number = number//10
        #For numbers out of range
        if number>2**31 or number<-2**31:
            return 0
    #Making positive number negative if it was a negative number at the start
    if is_negative:
        reverseNum = -reverseNum
    return reverseNum

def main():
    number:int = 89332
    print(reverseNumber(number))

if __name__ == "__main__":
    main()