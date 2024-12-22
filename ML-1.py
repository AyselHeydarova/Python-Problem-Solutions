data = open("test.txt", 'r').read().split()

resp = list(map(int, data))
firstList = resp[0::2]
secondList = resp[1::2]

firstList.sort()
secondList.sort()

print("Sorted firstList:", firstList)
print("Sorted secondList:", secondList)

merged = list(zip(firstList, secondList))

print(merged)


total = 0

for first, second in merged:
    total += first * secondList.count(first)


print(total)