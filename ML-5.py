first, second = open('test5.txt').read().split('\n\n')

rules = first.split()
updates = second.split()

print('rules', rules)
print('updates', updates)

def isCorrectOrder(update):
    isCorrect = True
    for rule in rules:
        one, two = rule.split('|')

        if one in update and two in update:
            if update.index(one) > update.index(two):
                isCorrect = False
    return isCorrect

total = 0
for upd in updates:
    update = upd.split(',')
    if isCorrectOrder(update):
        middle = update[(len(update) - 1) // 2]
        total+= int(middle)
print('total', total)

