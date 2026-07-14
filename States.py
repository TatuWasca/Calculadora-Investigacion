import tkinter as tk

class States:
    def __init__(self):
        self.dec   = tk.DoubleVar()
        self.cohen = tk.DoubleVar()

        self.dec.set("")
        self.cohen.set("")