from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize 
text = "Hello, world! This is a test."
sentences = sent_tokenize(text)
print(sentences)  # Output: ['Hello, world!', 'This is a test.']
words = word_tokenize(text)
print(words)  # Output: ['Hello', ',', 'world', '!', 'This',