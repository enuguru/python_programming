#!/usr/bin/env python3

# Chapter 16 -- GUI Example
# ------------------------------------------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# A quick Tkinter example. We won't dwell on this. But we need to establish
# a simple example that works.
# ::

import tkinter

class Application:
    def __init__( self, parent ):
        frame = Tkinter.Frame(parent)
        frame.pack()

        self.button = Tkinter.Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=Tkinter.LEFT)

        self.message= Tkinter.Label( root, text="Hello world" )
        self.message.pack(side=Tkinter.LEFT)

root= tkinter.Tk()
app= Application( root )
root.mainloop()
