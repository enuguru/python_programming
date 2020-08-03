
from tkinter import *

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# create button
button = Button(gui, text='My Button', width=40, height=3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
# add button to gui window
button.pack()

gui.mainloop()
