num = int(input("Enter a number: "))

def is_even(num):
    return (num % 2) == 0

if is_even(num):
    print(str(num) + " is an even number")
else:
    print(str(num) + " is an odd number")