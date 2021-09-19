def decimal_to_binary(n):
   if n > 1:
       decimal_to_binary(n//2)
   print(n % 2,end = '')

userInput = int(input('Enter the decimal number to find its binary equivalent: '))
print("The binary representation of", userInput, "is: ")
decimal_to_binary(userInput)
