best = 0

for a in range(1,101):
    for b in range(1,101):
        x = a**b
        charsum = sum([int(i) for i in list(str(x))])
        if charsum > best:
            best = charsum

print(best)
