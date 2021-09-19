def even_odd(numbers):
    even = []
    odd = []
    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

if __name__ == '__main__':
    userInput = input("Enter the numbers (space separated) to check: ")
    userInput = list(userInput.split())
    even, odd = even_odd(userInput)
    print('Even Nos: ', ','.join(even), '\n', 'Odd Nos: ', ','.join(odd))