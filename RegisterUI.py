import tkinter as tk
from tkinter import messagebox

class RegisterUI:

    def __init__(self, window, caller, player_manager):
        self.caller = caller
        self.player_manager = player_manager
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