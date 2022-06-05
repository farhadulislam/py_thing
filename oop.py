class Animal:
    def __init__(self):
        self.name = "This is an animal object"

    def showInfo(self):
        self.name = "Animal"


human = Animal()
human.showInfo()

