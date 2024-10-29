import tkinter as tk

from AddDeckUI import *

class MainUI:

    def __init__(self, window, caller, player):
        self.caller = caller
        self.player = player
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 500, height = 500, bg = "#78a090")
        self.canvas.pack()

        self.play_button = tk.Button(self.canvas, text = "Jugar")
        self.play_button.place(x = 10, y = 390)

        self.deck_button = tk.Button(self.canvas, text = "Crear Deck", command = self.toDeckCreation)
        self.deck_button.place(x = 100, y = 390)

        self.back_button = tk.Button(self.canvas, text = "Cerrar Sesión", command = self.back)
        self.back_button.place(x = 100, y = 390)

    def toDeckCreation(self):
        self.window.withdraw()
        deck_creation_window = tk.Toplevel()
        deck_creation_window.title("Creación de Decks")
        deck_creation_window.resizable(width = tk.NO, height = tk.NO)
        deck_creation_ui = AddDeckUI(deck_creation_window, self, self.player)
        deck_creation_ui.run()

    def run(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()