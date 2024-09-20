import random
import math

def generate_prime(bits):
    while True:
        potential_prime = random.randint(2**(bits-1), 2**bits - 1)
        if is_prime(potential_prime):
            return potential_prime

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def generate_keys(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)

    N = p * q
    phi_N = (p - 1) * (q - 1)

    e = generate_relative_prime(phi_N)
    
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
