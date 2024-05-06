import os
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("Launcher")
root.geometry("400x400")

class Button:
    def __init__(self, text, func, row, col, image=""):
        image2 = tk.PhotoImage(file="rl.png")
        image3 = image2.subsample(1, 1)
        self.button = ttk.Button(
            root,
            text=text,
            image=image3,
            compound = tk.LEFT,
            command=func)
        # self.button.pack()
        self.button.grid(row=row, column=col, sticky=tk.NW, pady=0)
        self.button.image = image3

    def open_text(text):
        os.startfile(text)


print(os.getcwd())
Button("Open example text", lambda x: Button.open_text("example_for_launch.txt"), 0, 0, image="notepad.PNG")
Button("Open example text 2", lambda x: Button.open_text("Hello World 2.txt"), 1, 0,  image="notepad.PNG")


root.mainloop()