
import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.geometry("400x200")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

labelExample = tk.Label(app, text="20", font=fontStyle)

pixelVirtual = tk.PhotoImage(width=2, height=2)

buttonExample1 = tk.Button(app,
                           text="Increase",
                           image=pixelVirtual,
                           width=300,
                           height=200,
                           compound="c")
buttonExample2 = tk.Button(app,
                           text="Decrease",
                           image=pixelVirtual,
                           width=300,
                           height=200,
                           compound="c")

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.RIGHT)
app.mainloop()
