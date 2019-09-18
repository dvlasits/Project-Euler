from functools import lru_cache

#@lru_cache(maxsize = 100000)
def numWays(total,availableValues,whatToMinus = None):
  if whatToMinus == None:
    return sum([numWays(total,availableValues,item) for item in availableValues])
  availableValues.remove(whatToMinus)
  total -= whatToMinus
  if total == 0:
    return 1
  if total < 0:
    return 0
  availableValues = list([i for i in availableValues if i <= total])
  return sum([numWays(total,availableValues,item) for item in availableValues])


available = [1/(i**2) for i in range(2,45+1)]
print(numWays(1/2,available))
