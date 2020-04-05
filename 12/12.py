from collections import defaultdict


def primeFactors(x):
    primes = defaultdict(int)

    start = 2
    while True:
        if x == 1:
            return primes
        if x%start == 0:
            primes[start] += 1
            x = x/start
        else:
            start += 1


    if x == 1:
        return primes
    if x%start == 0:
        primes[start] += 1
        return primeFactors(x/start,start,primes)
    return primeFactors(x,start+1,primes)

def numFactors(x):
    primes = primeFactors(x)
    prod = 1
    for prime in primes:
        prod *= primes[prime] +1
    return prod

tri = 0
count = 1


while True:
    tri += count
    #print(tri,numFactors(tri))
    if numFactors(tri) > 500:
        print(tri)
        break
    count += 1
