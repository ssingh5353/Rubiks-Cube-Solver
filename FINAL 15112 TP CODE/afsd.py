# Goldbach's Conjecture: every even number greater than 2 is the sum of two primes
# This conjecture seems to be right, but we've never been able to prove it.

def findGoldbachViolation():
    # halt if/when we find an even number > 2 that is not the sum of two primes
    def isPrime(n):
        if (n < 2): return False
        if (n == 2): return True
        if (n % 2 == 0): return False
        for factor in range(3,round(n**0.5)+1,2):
            if (n % factor == 0): return False
        return True
    def goldbachWorks(even):
        # return true if this even is the sum of two primes, false otherwise
        for p in range(2, even):
            if (isPrime(p) and (isPrime(even-p))):
                return True
        return False
    even = 4
    while True:
        if (not goldbachWorks(even)):
            print('Found the violation at even =', even)
            return False
        even += 2
    # never halt if Goldach's conjecture is True

if (halts(findGoldbachViolation, None)):
    print("Goldbach's Conjecture is False!")
else:
    print("Goldbach's Conjecture is True!")