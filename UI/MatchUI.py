from functools import partial

from UI.SubUI import *
from commons.ImageHandler import *

class MatchUI(SubUI):
    image_handler = ImageHandler()

    def __init__(self, window, caller, player):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        :caller: UI that called this one.
        :player_manager: manager for the players accounts info.
        :player: player that is currently logged in.
        """
        SubUI.__init__(self, window, caller, 800, 600)
        self.card_back = self.image_handler.resizeImage("back.jpg")

        self.placeOpponent(100, 20)

        self.placePlayer(100, self.height - 130)

    def placeOpponent(self, posX, posY):
        steps = 100
        
        self.opp_card1 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card1.place(x = posX, y = posY)

        self.opp_card2 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card2.place(x = posX + steps, y = posY)

        self.opp_card3 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card3.place(x = posX + 2*steps, y = posY)

        self.opp_card4 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card4.place(x = posX + 3*steps, y = posY)

        self.opp_card5 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card5.place(x = posX + 4*steps, y = posY)

        self.opp_card6 = tk.Label(self.canvas, image = self.card_back)
        self.opp_card6.place(x = posX + 5*steps, y = posY)

    def placePlayer(self, posX, posY):
        steps = 100
        card_back = self.image_handler.resizeImage("back.jpg")
        self.card1 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 0))
        self.card1.place(x = posX, y = posY)

        self.card2 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 1))
        self.card2.place(x = posX + steps, y = posY)

        self.card3 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 2))
        self.card3.place(x = posX + 2*steps, y = posY)

        self.card4 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 3))
        self.card4.place(x = posX + 3*steps, y = posY)

        self.card5 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 4))
        self.card5.place(x = posX + 4*steps, y = posY)

        self.card6 = tk.Button(self.canvas, image = self.card_back, command = partial(self.playCard, 5))
        self.card6.place(x = posX + 5*steps, y = posY)

    def playCard(self, index):
        print(index)