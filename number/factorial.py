def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

userInput = int(input())
print("The factorial of %d is %d" % (userInput, factorial(userInput)))