
import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x200')
        button = tk.Button(self.root,
                          text = 'Click and Quit',
                          command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

app = Test()
