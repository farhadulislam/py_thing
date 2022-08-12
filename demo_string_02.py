

sentence = ' this is a sentence. And, this is another sentence '
print(sentence.capitalize())
print(sentence.title())
print(sentence.endswith('sent'))
print(sentence.startswith(' '))
print(sentence.strip())
print(sentence.lstrip())
print(sentence.rstrip())
print(sentence.split())
print(sentence.count('s'))
print(sentence.index('sentence'))
print(sentence[::-1])
print(sentence)
print(sentence.capitalize())
print(sentence.swapcase())
print(sentence.replace('And', 'Also'))
sentence = ' this is a sentence. And, this is another sentence '


split_words = sentence.split()
print(split_words)
print(f"Type of split_words {type(split_words)}")
print(' '.join(split_words))
print(sentence.partition('And, this is another sentence '))
'''COUNT NUM OF WORDS : split() returns a list, we can then
use len() to get num of words'''
print(sentence.split())
print(len(sentence.split()))
print(sentence[-2])

list_words = [i for i in sentence.split() if i != ' ']
print(list_words)
print(len(list_words))

animal,species = 'fox', 'mammal'

print("The {1} is a {0}".format(species, animal))
print("The {} is a {}".format(animal, species))
# Key word arguments can also be used same way, look below
print("{plant} is a {plant_type}".format(plant="Pteridopyhta", plant_type ="Fern"))
text = "{} is a {}"
print(text.format("T2 phage", "bacterion"))


# str.format() - more advanced stuff

pi = 3.1415
number = 1000

print("The pi is {:.2f}".format(pi))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:e}".format(number))



