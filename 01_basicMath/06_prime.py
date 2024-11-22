from math import sqrt
def isPrime(num:int)->bool:
    if num<=1:return False
    count:int = 0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    return True if count==2 else False

def optimalIsPrime(num: int) -> bool:
    """
    Efficiently checks if a number is prime using square root optimization.
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Args:
        num (int): The number to check for primality
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Handle edge cases:
    # 1. Numbers less than or equal to 1 are not prime by definition
    if num <= 1: 
        return False
        
    # 2. 2 is the only even prime number
    if num == 2: 
        return True
        
    # 3. All other even numbers are not prime because 2 is a factor
    if num % 2 == 0: 
        return False
    
    # Main optimization: Only check odd numbers up to square root
    # Why square root? 
    # - If a number n is not prime, it must have a factor <= √n
    # - Because if a×b=n, and both a,b > √n, then a×b > n
    # Why odd numbers only?
    # - We already handled even numbers above
    # - This cuts our checks in half
    for i in range(3, int(num**0.5) + 1, 2):
        # If we find any number that divides evenly, it's not prime
        if num % i == 0:
            return False
    
    # If we haven't found any factors by now, the number is prime
    # Because:
    # 1. It's not ≤ 1
    # 2. It's not 2
    # 3. It's not even
    # 4. It has no odd factors up to its square root
    return True

# main function
def main()->None:
    num = 25
    print(f"\nComparing methods for number {num}:")
    
    print("\nOriginal method checks:")
    checks1 = 0
    for i in range(1, num+1):
        checks1 += 1
        if num % i == 0:
            print(f"Found factor: {i}")
    
    print(f"\nOptimized method checks:")
    checks2 = 0
    
    # Early checks
    checks2 += 3  # for num<=1, num==2, num%2==0
    print("Early checks: <=1, ==2, even?")
    
    # Main loop
    sqrt_n = int(num**0.5)
    print(f"Only checking up to sqrt({num}) = {sqrt_n}")
    for i in range(3, sqrt_n+1, 2):
        checks2 += 1
        print(f"Checking {i}")
        if num % i == 0:
            print(f"Found factor: {i}")
            break
    
    print(f"\nTotal checks in original method: {checks1}")
    print(f"Total checks in optimized method: {checks2}")
    print(f"Optimization reduced checks by: {((checks1-checks2)/checks1*100):.1f}%")

if __name__=='__main__':
    main()