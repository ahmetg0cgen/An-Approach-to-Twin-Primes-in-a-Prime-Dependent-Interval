from sympy import isprime, sieve

def has_twin_prime_between(p_k, p_k1):
    lower_bound = p_k * p_k1
    upper_bound = p_k1 ** 2
    
    # Find prime numbers in the specified range
    primes_in_range = [n for n in range(lower_bound + 1, upper_bound) if isprime(n)]
    
    # Check if twin is prime
    for i in range(len(primes_in_range) - 1):
        if primes_in_range[i+1] - primes_in_range[i] == 2:
            return True, (primes_in_range[i], primes_in_range[i+1])
    
    return False, None

def check_twin_primes_in_prime_intervals(N):
    primes = list(sieve.primerange(3, 10**6))[:N]  # Take the first N prime numbers, excluding 2 (the reason for excluding 2 is the referenced articles)
    results = []
    
    for i in range(len(primes) - 1):
        p_k, p_k1 = primes[i], primes[i+1]
        has_twin, twin_pair = has_twin_prime_between(p_k, p_k1)
        
        if has_twin:
            results.append(f"There is a twin prime in the range {p_k} * {p_k1}, {p_k1}^2: {twin_pair}")
        else:
            results.append(f"There is no twin prime in the range {p_k} * {p_k1}, {p_k1}^2.")
    
    return results

# Let's determine how many prime number pairs to check
N = 20  # Let's check the first 20 prime numbers (excluding 2)
results = check_twin_primes_in_prime_intervals(N)

for res in results:
    print(res)
