import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 500, height= 350)
        self.root = root
        self.pack()
        self.config(bg= 'gray')