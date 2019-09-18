# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# 180180

import math
def factors(x):
  # This function takes a number and prints the factors
  total = 0
  for i in range(1, math.ceil(x**0.5)):
    if x % i == 0:
      total += 1
  total += 1
  return math.ceil(total /2)

#for factor in factors(360):
#    print factor

# solve for 10
#
num = 2
num = 10000
while True:
  using = num**2
  l = factors(using)
  print(using,l)
  if l > 1000:
    print(num)
    break
  num += 1
