upTo = 10**6

dictP = {}
for i in range(2,upTo):
    dictP[i] = 0

count = 2
while count < upTo:
    if dictP[count] == -1:
        count += 1
        continue

    dictP[count] = 1
    start = 2*count
    while True:
        if start >= upTo:
            break
        dictP[start] = -1
        start += count
    count += 1

PrimeArr = [i for i in dictP if dictP[i] == 1]
PrimeArrSet = set(PrimeArr)

print("made all arrays")

cutting = 2
while True:
    going = cutting
    while going <= len(PrimeArr):
        primeSum = sum(PrimeArr[going-cutting:going])
        if primeSum in PrimeArrSet:
            print(primeSum,cutting,PrimeArr[going-cutting:going])
        going += 1
    cutting += 1
