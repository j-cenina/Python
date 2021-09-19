import re

def findLongestWord(str):
    pattern = re.compile('\S+')
    words = pattern.findall(str)

    wordLength = 0
    for word in words:
        if len(word) > wordLength:
            wordLength = len(word)
            
#    wordLength = len(max(words, key = len))    # This line can be used instead of the above for loop

    return wordLength

text = input()
result = findLongestWord(text)
print("The longest word in the string has a length of %s" % result)