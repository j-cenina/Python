upperLimit = int(input())

# A function to return the quark value of an integer
def quarkValue(n):
    if n == 1:
        return 1
    else:
        return bin(n).count('1') * n

# The solution to the challenge
def solution(n):
    print('The following list of quark pairs appears in the interval 1 to ' +
    str(upperLimit))
    print('___________________________________________________________________\n')
    item = 1
    while item <= n:
        nums = item + 1
        limit = item * 2 + 1
        if limit > n:
            limit = n
        while nums <= limit:
            if quarkValue(item) == quarkValue(nums):
                print(str(item) + ': ' + str(nums))
            nums += 1
        item += 1

solution(upperLimit)