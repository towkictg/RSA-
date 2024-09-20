
import random
import math

def generate_prime(bits):
    while True:
        potential_prime = random.randint(2**(bits-1), 2**bits - 1)
        if is_prime(potential_prime):
            return potential_prime

def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    
    # Iterate from 2 to the square root of the number
    # Checking divisibility by all numbers up to the square root is sufficient
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any number, it's not prime
    
    return True


def generate_keys(bits):
    p = 51421
    q = 49943
    while p == q:
        q = generate_prime(bits)

    N = p * q
    phi_N = (p - 1) * (q - 1)
    print('P:', p)
    print('Q:', q)
    
    print('Phi of N:', phi_N)

    e = 131
    
    d = pow(e, -1, phi_N)

    return (N, e), d

def generate_relative_prime(n):
    while True:
        potential_prime = random.randint(2, n)
        if math.gcd(n, potential_prime) == 1:
            return potential_prime

# Example usage:
bits = 16
public_key, private_key = generate_keys(bits)
print("Public key (N, e):", public_key)
print("Private key (d):", private_key)
