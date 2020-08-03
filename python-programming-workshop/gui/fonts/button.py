
from tkinter import *
import tkinter.font as font

gui = Tk(className='Gui for good students')
gui.geometry("500x200")

# define font
myFont = font.Font(family='Helvetica', size=30, weight='bold')

# create button
button = Button(gui, text='Aprameyas button', fg='Blue')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop()
