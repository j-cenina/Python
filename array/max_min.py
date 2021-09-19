number_data = [323, 209, 5900, 31092, 3402, 39803, 78341, 79843740, 895,
6749, 2870984]

def maxx(arg):
    num =float('-inf')
    for number in arg :
        if number > num:
            num = number 
    return "Max number is: {}".format(num)

print(maxx (number_data ))

def minn(arg):
    num =float('inf')
    for number in arg :
        if number < num:
            num = number 
    return "Min number is: {}".format(num)

print(minn (number_data ))