import sys
import math
from itertools import count


def slow_sieve(nmax):
    """
    Returns a list of prime numbers using Sieve of Atkin algorithm
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes

def medium_sieve(limit):
    """
    Returns a list of prime numbers using Sieve of Eratosthenes algorithm
    """
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

def fast_sieve(n):
    """
     Returns a list of prime numbers using Sieve Of Sundaram algorithm
    """
    nk = (n-1)//2
    ks = list(range(nk+1))
 
    for i in count(1):
        step  = 2*i+1
        start = i*(step + 1)
        if start > nk:
            break
         
        ks[start::step] = (0 for _ in range(start, nk+1, step))
 
    return [2] + [2*k+1 for k in filter(None, ks)]
    
