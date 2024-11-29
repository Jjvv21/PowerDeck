import tkinter as tk
import time, threading
from tkinter import messagebox

from UI.SubUI import *
from logic.EmparejamientoClient import *
from UI.AddDeckUI import *

class MainUI(SubUI):
    message = ""

    def __init__(self, window, caller, player_manager, player):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        :caller: UI that called this one.
        :player_manager: manager for the players accounts info.
        :player: player that is currently logged in.
        """
        SubUI.__init__(self, window, caller, 500, 500)
        self.caller = caller
        self.player_manager = player_manager
        self.player = player
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 500, height = 500, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(200, 5, anchor = tk.NW, text = "PowerDeck")
        self.canvas.create_text(190, 25, anchor = tk.NW, text = f"Bienvenido {self.player.getUser()}")

        self.play_button = tk.Button(self.canvas, text = "Jugar", command = self.findGame)
        self.play_button.place(x = 100, y = 80)
        self.canvas.create_text(150, 85, anchor = tk.NW, text = "", tags = "wait")

        self.deck_button = tk.Button(self.canvas, text = "Crear Deck", command = self.toDeckCreation)
        self.deck_button.place(x = 100, y = 110)

        self.back_button.config(text = "Cerrar Sesión")
        self.back_button.place(x = 420, y = 470)

    def findGame(self):
        self.play_button.config(state = tk.DISABLED)
        threading.Thread(target=self.looking).start()
        threading.Thread(target=self.showWaitTime).start()

    def looking(self):
        self.message = connect()
        self.play_button.config(state = tk.NORMAL)
        messagebox.showinfo("Éxito", self.message)
        self.message = ""

    def showWaitTime(self):
        start_time = time.time()
        while (self.message == "") and (time.time() - start_time < 60):
            wait = time.time() - start_time
            self.canvas.itemconfig("wait", text = f"Tiempo de expera: {int(wait)}s")
        self.canvas.itemconfig("wait", text = "")

    def toDeckCreation(self):
        """
        toDeckCreation hides this UI and proceeds to the Deck Creation UI.
        """
        self.window.withdraw()
        deck_creation_window = tk.Toplevel()
        deck_creation_window.title("Creación de Decks")
        deck_creation_window.resizable(width = tk.NO, height = tk.NO)
        deck_creation_ui = AddDeckUI(deck_creation_window, self, self.player_manager, self.player)
        deck_creation_ui.run()

    def back(self):
        """
        back returns to the UI that called this one.
        """
        self.player_manager.save()
        self.window.destroy()
        self.caller.window.deiconify()