def insertion_sort(l):
    result = l[:]
    lengthData = len(result)
    start = 1

    while start <= lengthData - 1:
        if result[start] < result[start - 1]:
            value = result.pop(start)

            # find insertion point
            for i in range(start):
                if result[i] > value:
                    result.insert(i, value)
                    break
        start += 1
    return result

list = [33, 20, 12, 31, 2, 67]
print(insertion_sort(list))
