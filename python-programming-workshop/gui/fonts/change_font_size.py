
from tkinter import *
import tkinter.font as font

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# define font
myFont = font.Font(family='Arial')
myFont = font.Font(size=50)

# create button
button = Button(gui, height=25, width=50, text='My Button', bg='blue', fg='red')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop()
