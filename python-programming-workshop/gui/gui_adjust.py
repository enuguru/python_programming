
import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.geometry("600x500")

def decreaseSize():
    buttonExample1.configure(height = 100,
                             width = 100)

def increaseSize():
    buttonExample2.configure(height = 400,
                             width = 400)

pixelVirtual = tk.PhotoImage(width=1, height=1)

buttonExample1 = tk.Button(app,
                           text="Decrease Size",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound="c",
                           command = decreaseSize)
buttonExample2 = tk.Button(app,
                           text="Increase Size",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound=tk.CENTER,
                           command = increaseSize)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.RIGHT)
app.mainloop()
