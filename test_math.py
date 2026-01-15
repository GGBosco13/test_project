import math

def get_prime_factors(n):
    """Returns a list of prime factors for a given integer n."""
    factors = []
    
    # Handle the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # n must be odd at this point. So we can skip one element (Note i = i + 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
            
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
        
    return factors

def main():
    """Entry point of the script."""
    numbers_to_test = [12, 49, 1050, 395]
    
    print("--- Prime Factorization Results ---")
    for num in numbers_to_test:
        factors = get_prime_factors(num)
        # Using an f-string for clean formatting (similar to printf)
        print(f"Number: {num:4} | Factors: {factors}")

