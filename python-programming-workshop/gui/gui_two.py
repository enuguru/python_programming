
import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.geometry("400x200")

buttonExample1 = tk.Button(app,
                           text="Aprameya",
                           width=15,
                           height=10)
buttonExample2 = tk.Button(app,
                           text="Hrishi",
                           width=10,
                           height=10)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.RIGHT)

app.mainloop()
