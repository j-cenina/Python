# Function to reverse a string
def reverseString(str):
    return str[::-1]

text = input()
print("The string you entered is:      %s" % text)
print("The reverse of this string is:  %s" % reverseString(text))