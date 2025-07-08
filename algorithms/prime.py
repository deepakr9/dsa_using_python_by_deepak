# Sieve of Eratosthenes
# this algorithm is used to find prime numbers in the given range N
# Time complexity
import math
def primes(num):
  is_prime = [True] * num
  is_prime[0:2] = [False, False]
  for i in range(2, int(math.sqrt(num))+1):
    if is_prime[i]:
      for j in range(i*i, num, i):
        is_prime[j] = False
  return [i for i, x in enumerate(is_prime) if x]
print(primes(20))



