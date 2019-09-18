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
  test = [q for q in combinations(possible2, 2) if q[0].isdisjoint(q[1]) and len(q[0]) == len(q[1]) and len(q[0])!= 1]
  print(test)
  print(len(test))

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

def whatneedsChecking(sett):
  possiblecombs = []
  setts = set(sett)
  for i in range(1,len(sett)):
    possiblecombs.append([set(q) for q in combinations(sett, i)])

  possible2 = []
  for row in possiblecombs:
    for item in row:
      possible2.append(item)

  pairs = [1 for q in combinations(possible2, 2) if q[0].isdisjoint(q[1]) and sum(q[0]) == sum(q[1])]
  test = [q for q in combinations(possible2, 2) if q[0].isdisjoint(q[1]) and len(q[0]) == len(q[1]) and len(q[0])!= 1]
  refresh = []
  for item in test:
    item1,item2 = item
    if max(item1) < min(item2) or max(item2) < min(item1):
      pass
    else:
      refresh.append(item)
  finalrefresh = []
  for item in refresh:
    item1,item2 = item
    test1 = list(item1)
    test2 = list(item2)
    test1.sort()
    test2.sort()
    doneOneWay = 0
    doneSecondWay = 0
    for i,j in zip(test1,test2):
      if i > j:
        doneSecondWay = 1
      if j > i:
        doneOneWay = 1
    if doneOneWay == 1 and doneSecondWay == 1:
      finalrefresh.append(item)
  print(len(finalrefresh))




sett = [1,2,3,4,5,6,7,8,9,10,11,12]
whatneedsChecking(sett)
