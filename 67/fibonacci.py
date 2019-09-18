from functools import lru_cache



@lru_cache(maxsize = 100000)
def fib(n):
  global counter
  counter += 1
  if n == 1 or n == 2:
    return 1
  return fib(n-1) + fib(n-2)

print(fib(35))
