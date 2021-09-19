def largestOfFour(arrList):
    result  = []
    maxItem = 0
    for each in arrList:
        maxItem = max(each)
        result.append(maxItem)

    return result

arr = [4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]
print(largestOfFour(arr))
