import os
import shutil

path = "C:\\Farhad\\Nemo\\LEARNING\\LAB\\"
if os.path.exists(path):
    print("Location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("The location doesn't exists")

###########################################################

# Read a file's content
print("DEMO : READING A FILE")
try:
    with open("test.txt") as file_to_read:
        print(file_to_read.read())
except FileNotFoundError:
    print("File wasn't found")


###########################################################

# Writing to or appending to a file's content
print("DEMO : WRITING A FILE")
back_up_text = " File \nDate: 15 Aug 2022\nThis is test file. \nPython, Java, C\n "
text = "This a new line\nThis is another new line"
try:
    with open("test.txt", 'a') as file_to_write: #  use 'w' to overwrite the existing contents such as -> with open("test.txt", 'r') as file_to_write:
        print(file_to_write.write(text))
except FileNotFoundError:
    print("File wasn't found")


######################### COPYING FILES #######################

shutil.copyfile("test.txt", "test_copy.txt")
shutil.copy("test.txt", "test_copy.txt")
shutil.copy2("test.txt", "test_copy.txt")

