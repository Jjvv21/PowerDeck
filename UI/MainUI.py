import tkinter as tk
import time, threading
from tkinter import messagebox

from UI.SubUI import *
from logic.EmparejamientoClient import *
from UI.AddDeckUI import *
from UI.MatchUI import *

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
        self.player_manager = player_manager
        self.player = player

        self.canvas.create_text(200, 5, anchor = tk.NW, text = "PowerDeck")
        self.canvas.create_text(190, 25, anchor = tk.NW, text = f"Bienvenido {self.player.getUser()}")

        self.play_button = tk.Button(self.canvas, text = "Jugar", command = self.findGame)
        self.play_button.place(x = 100, y = 80)
        self.canvas.create_text(200, 85, anchor = tk.NW, text = "", tags = "wait")
        self.cancel_button = tk.Button(self.canvas, text = "Cancelar", command = self.cancelSearch)
        self.cancel_button.place(x = 1000, y = 1000)

        self.match_button = tk.Button(self.canvas, text = "Partida", command = self.toMatch)
        self.match_button.place(x = 100, y = 200)

        self.deck_button = tk.Button(self.canvas, text = "Crear Deck", command = self.toDeckCreation)
        self.deck_button.place(x = 100, y = 110)

        self.back_button.config(text = "Cerrar Sesión")
        self.back_button.place(x = 420, y = 470)

    def findGame(self):
        self.play_button.place(x = 1000, y = 1000)
        self.cancel_button.place(x = 100, y = 80)
        threading.Thread(target = self.looking).start()
        threading.Thread(target = self.showWaitTime).start()

    def cancelSearch(self):
        self.cancel_button.place(x = 1000, y = 1000)
        self.cancel = True
        self.play_button.place(x = 100, y = 80)

    def looking(self):
        self.message = connect()
        self.cancel_button.place(x = 1000, y = 1000)
        self.play_button.place(x = 100, y = 80)
        messagebox.showinfo("Éxito", self.message)
        self.message = ""

    def showWaitTime(self):
        self.cancel = False
        start_time = time.time()
        while (self.message == "") and (time.time() - start_time < 60) and not self.cancel:
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

    def toMatch(self):
        """
        toDeckCreation hides this UI and proceeds to the Deck Creation UI.
        """
        if self.player.getSelectedDeck() != None:
            self.window.withdraw()
            match_window = tk.Toplevel()
            match_window.title("Creación de Decks")
            match_window.resizable(width = tk.NO, height = tk.NO)
            match_ui = MatchUI(match_window, self, self.player)
            match_ui.run()
        else:
            messagebox.showerror("Error", "seleccione un Deck para la partida")


    def back(self):
        """
        back returns to the UI that called this one.
        """
        self.player_manager.save()
        self.window.destroy()
        self.caller.window.deiconify()