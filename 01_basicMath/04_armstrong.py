def isArmstrong(num: int) -> bool:
    duplicate: int = num
    if num < 0:
        return False
        
    # Calculate digit count once before the loop
    count: int = len(str(num))
    poweredNum: int = 0
    
    while num > 0:
        lastDigit: int = num % 10
        poweredNum += pow(lastDigit, count)  # Use lastDigit instead of num
        num = num // 10
        
        if poweredNum < -2**31 or poweredNum > 2**31:
            return False
            
    return poweredNum == duplicate

def main() -> None:
    num: int = 371
    print(isArmstrong(num))

if __name__ == "__main__":
    main()