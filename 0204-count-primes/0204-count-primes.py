class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes = 0
        is_prime = [False, False] + [True] * (n - 2)
        
        for p in range(2, n):
            if is_prime[p]:
                primes += 1
                # Seive out the multiples of p
                for i in range(p, n, p):
                    is_prime[i] = False
        
        return primes
        