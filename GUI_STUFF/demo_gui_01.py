from tkinter import *

window = Tk()

window.geometry("420x420")
window.title("Farhad Islam")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config(background ="green")
window.mainloop()

def display_mishu():
    mishu = Tk()

    mishu.geometry("420x420")
    mishu.title("Foyjunnesa Mishkat")
    icon = PhotoImage(file='icon.png')
    mishu.iconphoto(True,icon)
    mishu.config(background ="pink")
    mishu.mainloop()

counter = 0
while(counter<=10):
    display_mishu()
    counter +=1