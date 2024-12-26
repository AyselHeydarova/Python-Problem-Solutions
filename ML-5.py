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

def correctOrder(update):
    print('update', update)

    for rule in rules:
        one, two = rule.split('|')

        if one in update and two in update:
            firstIndex = update.index(one)
            secondIndex = update.index(two)

            if firstIndex > secondIndex:
                update[secondIndex] = one
                update[firstIndex] = two

                if isCorrectOrder(update):
                    return  update
                else:
                    correctOrder(update)
                print('new update', update)

    return update

total = 0
for upd in updates:
    update = upd.split(',')
    if isCorrectOrder(update):
        middle = update[(len(update) - 1) // 2]
        # total+= int(middle)
    else:
        newUpdate = correctOrder(update)
        middle = update[(len(newUpdate) - 1) // 2]
        total += int(middle)
print('total', total)

