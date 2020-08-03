
from tkinter import *
import tkinter.font as font

gui = Tk(className='Your Python Examples - Button')
gui.geometry("300x100")

# define font
myFont = font.Font(family='Helvetica')

# create button
button = Button(gui, height=110, width=79, text='My Button', fg='red')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop()
