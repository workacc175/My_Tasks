import math

def is_prime(n):
    # 1. Handle numbers less than 2 (not prime)
    if n < 2:
        return False
    
    # 2. Check for the only even prime number
    if n == 2:
        return True
    
    # 3. Eliminate all other even numbers early
    if n % 2 == 0:
        return False

    # 4. Check odd divisors from 3 up to the square root of n
    # We use the square root because if n = a * b, one of those 
    # factors must be less than or equal to the square root.
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True

# Examples:
print(is_prime(11)) # Output: True
print(is_prime(15)) # Output: False