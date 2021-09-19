def check_prime(number):
    isPrime = False
    if number == 2:
        print(number, 'is a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                isPrime = False
                break
            else:
                isPrime = True

        if isPrime:
            print(number, 'is a Prime Number')

userInput = int(input('Enter a number to check: '))
check_prime(userInput)