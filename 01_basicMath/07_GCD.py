def GCD_iterative(n1:int,n2:int)->int:
    gcd:int = 1
    # Loop from 1 to the minimum of n1 and n2
    for i in range(1,min(n1,n2)+1):
        # Check if i is a divisor of both n1 and n2
        if(n1%i ==0 and n2%i==0):
            gcd = i
    # Return the greatest common divisor found
    return gcd

# Reverse loop method to find GCD
# Starts from the minimum of n1 and n2 and goes downwards
# More efficient as it stops once the largest divisor is found
def GCD_reverse(n1:int, n2:int)->int:
    for i in range(min(n1,n2),0,-1):
        # Check if i is a divisor of both n1 and n2
        if(n1%i==0 and n2%i==0):
            return i
    # Return 1 if no other common divisor is found
    return 1

# Euclidean algorithm for finding GCD
# This is the most efficient method
def findGCD(num1:int,num2:int)->int:
    # Continue until one of the numbers becomes zero
    while(num1>0 and num2>0):
        # Replace the larger number with its remainder when divided by the smaller number
        if(num1>num2):
            num1 = num1%num2
        else:
            num2 = num2%num1
    # Return the non-zero number, which is the GCD
    if (num1==0):
        return num2
    return num1

# Main function to test the GCD functions
def main()->None:
    # Test the GCD functions with example numbers
    n1, n2 = 48, 36
    print(f"GCD of {n1} and {n2}:")
    print(f"Using iterative method: {GCD_iterative(n1, n2)}")
    print(f"Using reverse method: {GCD_reverse(n1, n2)}")
    print(f"Using Euclidean algorithm: {findGCD(n1, n2)}")

if __name__=='__main__':
    main()