print("Hello, World!")

a = "Hello World! Tokenisation Example."
tokens = a.split()
print(tokens)

#text = "apple,mango-orange:banana?"

# Replace delimiters with spaces
#delimiters = ",:-?"
#or d in delimiters:
#    text = text.replace(d, " ")

#tokens = text.split()
#print(tokens)

#chars = [ch for ch in text]
#print(chars)

import re

text = "Hello, how are you?"

tokens = re.findall(r"\w+|\S", text)
print(tokens)
