def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print('Decimal equivalent of {} is {}'.format(binary1, decimal))

userInput = int(input('Enter the binary number to check its decimal equivalent: '))
binary_to_decimal(userInput)