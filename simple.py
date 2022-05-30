def doSth(apple):
    print(apple)

doSth("apple")

def showMyName():
    print("Farhad")

showMyName()

likes = input()
dislikes = input()
views = input()
rank = (((likes-dislikes)/views)*100)*(((likes-dislikes)/(likes+dislikes))*100)
print(rank)



