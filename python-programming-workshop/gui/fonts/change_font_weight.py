
from tkinter import *
import tkinter.font as font

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# define font
myFont = font.Font(family='Arial', size=30, weight='bold')

# create button
button = Button(gui, height=110, width=79, text='My Button', bg='blue', fg='red')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop()
