import sys
items = [4, 1, -3, 12, 5, 3, -6, 2]

def countingSort(lst):
    items = list(lst)
    min = sys.maxsize
    max = -sys.maxsize

    for x in lst:
        if x > max: max = x
        if x < min: min = x

    counts = [0] * (max - min + 1)
    for x in lst:
        counts[x - min] += 1

    total = 0
    for i in range(min, max + 1):
        oldCount = counts[i - min]
        counts[i - min] = total
        total += oldCount

    for x in lst:
        items[counts[x - min]] = x
        counts[x - min] += 1

    return items

sortItems = countingSort(items)
print(items)
print(sortItems)