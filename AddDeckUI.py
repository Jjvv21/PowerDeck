import tkinter as tk
from tkinter import messagebox

class AddDeckUI:

    def __init__(self, window, caller, player):
        self.caller = caller
        self.player = player
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 500, height = 300)
        self.canvas.pack()

        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 440, y = 270)

    def run(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()