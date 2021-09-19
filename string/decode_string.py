# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

import re

def decode(code):
    return "".join([x[-1] * int(x[:-1]) for x in re.findall(r'\d+\D', code)])

a = "2a5b3cd"
b = "3ab2c3d"

print(decode(a))
print(decode(b))