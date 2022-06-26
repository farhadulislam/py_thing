from enum import Enum

class Colour(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

colour = Colour(input("Enter a colut"))

if Colour.RED:
    print("Red chosen")
if Colour.GREEN:
    print("Green")

# Python 3.7 doesn't support match.
#match colour:
    #case Colour.RED:
        #print("Red")
