import math
from itertools import combinations



def checkSums(sett):
  possiblecombs = []
  setts = set(sett)
  for i in range(1,len(sett)):
    possiblecombs.append([set(q) for q in combinations(sett, i)])

  possible2 = []
  for row in possiblecombs:
    for item in row:
      possible2.append(item)


  pairs = [1 for q in combinations(possible2, 2) if q[0].isdisjoint(q[1]) and sum(q[0]) == sum(q[1])]

  if sum(pairs) > 0:
    return False
  return True

def checkLargerBigger(sett):
  here = list(sett)
  here.sort()
  runningTotalLower = here.pop(0)
  runningTotalHigher = 0
  for i in range(math.ceil((len(here)+1)/2)-1):
    runningTotalLower+= here.pop(0)
    runningTotalHigher+= here.pop(-1)
    if runningTotalHigher > runningTotalLower:
      return False
  return True

sett = [11, 18, 19, 20, 22,25]
initalguess = []
midNum = sett[math.floor(len(sett)/2)]
sett.insert(0,0)
sett = [i+midNum for i in sett]
print(sett)

best = 1000000000
'''[20, 31, 38, 39, 40, 42, 45]'''
for a in range(-5,6):
  print("a =", a)
  for b in range(-5,6):
    print("b =",b)
    for c in range(-5,6):
      for d in range(-5,6):
        for e in range(-5,6):
          for f in range(-5,6):
            for g in range(-5,6):
              newlist = list(sett)
              newlist[0] += a
              newlist[1] += b
              newlist[2] += c
              newlist[3] += d
              newlist[4] += e
              newlist[5] += f
              newlist[6] += g
              if sum(newlist) >= best:
                continue
              if len(newlist) > len(set(newlist)):
                continue
              if checkLargerBigger(newlist) and checkSums(newlist):
                best = sum(newlist)
                print(newlist)
                print(best)
