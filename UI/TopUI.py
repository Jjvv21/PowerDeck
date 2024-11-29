import tkinter as tk

class TopUI:

    def __init__(self, window, width, height):
        """
        Constructor that intializes and places the common widgets of the UI.

        :window: Toplevel container for the widgets.
        :width: int with the width for the window.
        :height: int with the height for the window.
        """
        self.window = window
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.window, width = self.width, height = self.height, bg = "#78a090")
        self.canvas.pack()

    def run(self):
        """
        run runs the main loop of the UI.
        """
        self.window.mainloop()