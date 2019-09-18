from functools import lru_cache



@lru_cache(maxsize = 100000)
def fib(n):
  if n == 1 or n == 2:
    return 1
  return fib(n-1) + fib(n-2)

counter = 1
print(fib(1))
while True:
  num = fib(counter)
  if len(str(num)) == 1000:
    print(counter)
    break
  counter += 1
