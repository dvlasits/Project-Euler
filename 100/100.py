b = 15
total = 21

'''xn+1 = 3 ⁢xn + 2 ⁢yn - 1
yn+1 = 4 ⁢xn + 3 ⁢yn - 1'''

while total < 10**12:
  bnew= 3*b+2*total - 2
  totalnew = 4*b + 3*total - 3
  b = bnew
  total = totalnew

print(b)
