import turtle


class Animal:
    def __init__(self):
        self.name = "This is an animal object"

    def showInfo(self):
        self.name = "Animal"


human = Animal()
human.showInfo()

tt = turtle.Turtle()
tt.circle(100)


