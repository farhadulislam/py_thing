

sentence = ' this is a sentence. And, this is another sentence '
print(sentence.capitalize())
print(sentence.title())
print(sentence.endswith('sent'))
print(sentence.startswith(' '))
print(sentence.strip())
print(sentence.split())
print(sentence.count('s'))
print(sentence.index('sentence'))
print(sentence[::-1])
print(sentence)
print(sentence.capitalize())
print(sentence.swapcase())
print(sentence.replace('And', 'Also'))
sentence = ' this is a sentence. And, this is another sentence '
print(sentence.lstrip())
print(sentence.rstrip())

split_words = sentence.split()
print(split_words)
print(' '.join(split_words))
print(sentence.partition('And, this is another sentence '))
'''COUNT NUM OF WORDS : split() returns a list, we can then
use len() to get num of words'''
print(sentence.split())
print(len(sentence.split()))