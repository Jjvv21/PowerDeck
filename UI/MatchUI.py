import time, threading, random
from functools import partial
from random import randint
from copy import deepcopy

from UI.SubUI import *
from commons.ImageHandler import *
from logic.CardAlbum import *

class MatchUI(SubUI):
    image_handler = ImageHandler()
    my_hand = [None, None, None, None, None, None]
    hand_image_names = ["noCard.jpg", "noCard.jpg", "noCard.jpg", "noCard.jpg", "noCard.jpg", "noCard.jpg"]
    hand_images = [None, None, None, None, None, None]
    stats = ["Poder", "Velocidad", "Magia", "Defensa", "Inteligencia", "Altura", "Fuerza", "Agilidad",
            "Salto", "Resistencia", "Flexibilidad", "Explosividad", "Carisma", "Habilidad", "Balance", 
            "Sabiduría", "Suerte", "Coodinación", "Amabilidad", "Lealtad", "Disciplina", "Liderazgo", 
            "Prudencia", "Confianza", "Percepción", "Valentía"]
    checking = -1
    turn_time = 30
    selected_card = None
    opp_selection = None
    wins = 0
    losses = 0
    turns = 7
    current_turn = 0

    def __init__(self, window, caller, player):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        :caller: UI that called this one.
        :player: player that is currently logged in.
        """
        SubUI.__init__(self, window, caller, 800, 600)
        self.player = player
        
        self.back_button.place(x = 1000, y = 1000)
        self.card_back = self.image_handler.resizeImage("back.jpg", 3)
        self.selected_card_image = self.image_handler.resizeImage("noCard.jpg", 2)
        self.opp_selection_image = self.image_handler.resizeImage("noCard.jpg", 2)
        self.canvas.create_text(300, 150, anchor = tk.NW, text = "Empezando partida...", tags = "feed")
        self.canvas.create_text(15, 250, anchor = tk.NW, text = "Tiempo: ")
        self.canvas.create_text(30, 270, anchor = tk.NW, text = f"{self.turn_time}s", tags = "time")
        self.canvas.create_image(150, 220, anchor = tk.NW, image = self.selected_card_image, tags = "mycard")
        self.canvas.create_image(550, 220, anchor = tk.NW, image = self.opp_selection_image, tags = "oppcard")

        self.placeOpponent(100, 20)
        self.placePlayer(100, self.height - 130)
        self.updateHand("start")

        self.my_deck = deepcopy(self.player.getSelectedDeck().getCards())
        random.shuffle(self.my_deck)
        for i in range(0, 5):
            self.my_hand[i] = self.my_deck.pop(0)
        self.updateHand("start")

        self.createBotDeck()

        threading.Thread(target=self.startTurn).start()

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

        info_offset_x = 85
        num_offset_x = 30
        stat_offset_y = 75
        tp_offset_y = 50
        bp_offset_y = 25


        self.canvas.create_text(posX - info_offset_x, posY - stat_offset_y, anchor = tk.NW, text = "Atributo:", tags = "stat")
        self.canvas.create_text(posX - info_offset_x, posY - tp_offset_y, anchor = tk.NW, text = "Turno de Poder:")
        self.canvas.create_text(posX - info_offset_x, posY - bp_offset_y, anchor = tk.NW, text = "Bonus:")


        self.card1 = tk.Button(self.canvas, command = partial(self.playCard, 0), state = tk.DISABLED)
        self.card1.place(x = posX, y = posY)
        self.canvas.create_text(posX + num_offset_x, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat1")
        self.canvas.create_text(posX + num_offset_x, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp1")
        self.canvas.create_text(posX + num_offset_x, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp1")


        self.card2 = tk.Button(self.canvas, command = partial(self.playCard, 1), state = tk.DISABLED)
        self.card2.place(x = posX + steps, y = posY)
        self.canvas.create_text(posX + num_offset_x + steps, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat2")
        self.canvas.create_text(posX + num_offset_x + steps, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp2")
        self.canvas.create_text(posX + num_offset_x + steps, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp2")

        self.card3 = tk.Button(self.canvas, command = partial(self.playCard, 2), state = tk.DISABLED)
        self.card3.place(x = posX + 2*steps, y = posY)
        self.canvas.create_text(posX + num_offset_x + 2*steps, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat3")
        self.canvas.create_text(posX + num_offset_x + 2*steps, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp3")
        self.canvas.create_text(posX + num_offset_x + 2*steps, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp3")

        self.card4 = tk.Button(self.canvas, command = partial(self.playCard, 3), state = tk.DISABLED)
        self.card4.place(x = posX + 3*steps, y = posY)
        self.canvas.create_text(posX + num_offset_x + 3*steps, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat4")
        self.canvas.create_text(posX + num_offset_x + 3*steps, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp4")
        self.canvas.create_text(posX + num_offset_x + 3*steps, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp4")

        self.card5 = tk.Button(self.canvas, command = partial(self.playCard, 4), state = tk.DISABLED)
        self.card5.place(x = posX + 4*steps, y = posY)
        self.canvas.create_text(posX + num_offset_x + 4*steps, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat5")
        self.canvas.create_text(posX + num_offset_x + 4*steps, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp5")
        self.canvas.create_text(posX + num_offset_x + 4*steps, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp5")

        self.card6 = tk.Button(self.canvas, command = partial(self.playCard, 5), state = tk.DISABLED)
        self.card6.place(x = posX + 5*steps, y = posY)
        self.canvas.create_text(posX + num_offset_x + 5*steps, posY - stat_offset_y, anchor = tk.NW, text = "_", tags = "stat6")
        self.canvas.create_text(posX + num_offset_x + 5*steps, posY - tp_offset_y, anchor = tk.NW, text = "_", tags = "tp6")
        self.canvas.create_text(posX + num_offset_x + 5*steps, posY - bp_offset_y, anchor = tk.NW, text = "_", tags = "bp6")

    def updateHand(self, action):
        for i in range(0, 6):
            if self.my_hand[i] != None:
                self.hand_image_names[i] = self.my_hand[i].getImage()
            else:
                self.hand_image_names[i] = "noCard.jpg"
            self.hand_images[i] = self.image_handler.resizeImage(self.hand_image_names[i], 3)
        self.card1.config(image = self.hand_images[0])
        self.card2.config(image = self.hand_images[1])
        self.card3.config(image = self.hand_images[2])
        self.card4.config(image = self.hand_images[3])
        self.card5.config(image = self.hand_images[4])
        self.card6.config(image = self.hand_images[5])
        if self.checking != -1 and action != "play":
            self.canvas.itemconfig("stat1", text = f"{self.my_hand[0].getStats()[self.checking]}")
            self.canvas.itemconfig("stat2", text = f"{self.my_hand[1].getStats()[self.checking]}")
            self.canvas.itemconfig("stat3", text = f"{self.my_hand[2].getStats()[self.checking]}")
            self.canvas.itemconfig("stat4", text = f"{self.my_hand[3].getStats()[self.checking]}")
            self.canvas.itemconfig("stat5", text = f"{self.my_hand[4].getStats()[self.checking]}")
            self.canvas.itemconfig("stat6", text = f"{self.my_hand[5].getStats()[self.checking]}")

            self.canvas.itemconfig("tp1", text = f"{self.my_hand[0].getTurnPower()}")
            self.canvas.itemconfig("tp2", text = f"{self.my_hand[1].getTurnPower()}")
            self.canvas.itemconfig("tp3", text = f"{self.my_hand[2].getTurnPower()}")
            self.canvas.itemconfig("tp4", text = f"{self.my_hand[3].getTurnPower()}")
            self.canvas.itemconfig("tp5", text = f"{self.my_hand[4].getTurnPower()}")
            self.canvas.itemconfig("tp6", text = f"{self.my_hand[5].getTurnPower()}")

            self.canvas.itemconfig("bp1", text = f"{self.my_hand[0].getBonusPower()}")
            self.canvas.itemconfig("bp2", text = f"{self.my_hand[1].getBonusPower()}")
            self.canvas.itemconfig("bp3", text = f"{self.my_hand[2].getBonusPower()}")
            self.canvas.itemconfig("bp4", text = f"{self.my_hand[3].getBonusPower()}")
            self.canvas.itemconfig("bp5", text = f"{self.my_hand[4].getBonusPower()}")
            self.canvas.itemconfig("bp6", text = f"{self.my_hand[5].getBonusPower()}")
        else:
            self.canvas.itemconfig("stat1", text = "_")
            self.canvas.itemconfig("stat2", text = "_")
            self.canvas.itemconfig("stat3", text = "_")
            self.canvas.itemconfig("stat4", text = "_")
            self.canvas.itemconfig("stat5", text = "_")
            self.canvas.itemconfig("stat6", text = "_")

            self.canvas.itemconfig("tp1", text = "_")
            self.canvas.itemconfig("tp2", text = "_")
            self.canvas.itemconfig("tp3", text = "_")
            self.canvas.itemconfig("tp4", text = "_")
            self.canvas.itemconfig("tp5", text = "_")
            self.canvas.itemconfig("tp6", text = "_")

            self.canvas.itemconfig("bp1", text = "_")
            self.canvas.itemconfig("bp2", text = "_")
            self.canvas.itemconfig("bp3", text = "_")
            self.canvas.itemconfig("bp4", text = "_")
            self.canvas.itemconfig("bp5", text = "_")
            self.canvas.itemconfig("bp6", text = "_")

    def createBotDeck(self):
        self.opp_deck = []
        album = CardAlbum()
        cards = album.getCards()
        random.shuffle(cards)
        URs = []
        MRs = []
        Rs = []
        Ns = []
        Bs = []
        for i in cards:
            if i.isMain() and i.gameActive() and i.pullActive():
                rarity = i.getRarity()
                match rarity:
                    case "Ultra-Rara":
                        URs.append(i)
                    case "Muy Rara":
                        MRs.append(i)
                    case "Rara":
                        Rs.append(i)
                    case "Normal":
                        Ns.append(i)
                    case "Básica":
                        Bs.append(i)

        while len(self.opp_deck) < 15:
            rng = random.randint(1, 100)
            if rng <= 5 and len(URs) > 0:
                self.opp_deck.append(URs.pop(0))
            elif rng <= 17 and len(MRs) > 0:
                self.opp_deck.append(MRs.pop(0))
            elif rng <= 35 and len(Rs) > 0:
                self.opp_deck.append(Rs.pop(0))
            elif rng <= 60 and len(Ns) > 0:
                self.opp_deck.append(Ns.pop(0))
            else:
                self.opp_deck.append(Bs.pop(0))

    def startTurn(self):
        self.checking = randint(0, len(self.stats))
        self.canvas.itemconfig("feed", text = f"Batalla por {self.stats[self.checking]}")
        self.current_turn += 1
        time.sleep(5)
        self.selectTime()

    def enableCards(self):
        self.card1.config(state = tk.NORMAL)
        self.card2.config(state = tk.NORMAL)
        self.card3.config(state = tk.NORMAL)
        self.card4.config(state = tk.NORMAL)
        self.card5.config(state = tk.NORMAL)
        self.card6.config(state = tk.NORMAL)

    def disableCards(self):
        self.card1.config(state = tk.DISABLED)
        self.card2.config(state = tk.DISABLED)
        self.card3.config(state = tk.DISABLED)
        self.card4.config(state = tk.DISABLED)
        self.card5.config(state = tk.DISABLED)
        self.card6.config(state = tk.DISABLED)

    def selectTime(self):
        self.canvas.itemconfig("stat", text = f"{self.stats[self.checking]}:")
        self.drawCard()
        self.canvas.itemconfig("feed", text = "Selección de carta")
        self.enableCards()
        start_time = time.time()
        wait = 0
        while (self.selected_card == None) and (time.time() - start_time < self.turn_time):
            wait = time.time() - start_time
            self.canvas.itemconfig("time", text = f"{int(self.turn_time - wait)}s")
        self.disableCards()
        if self.selected_card == None:
            self.playCard(randint(0, 5))
        self.canvas.itemconfig("stat", text = "Atributo:")
        self.opp_selection = self.opp_deck.pop(0)
        self.opp_selection_image = self.image_handler.resizeImage(self.opp_selection.getImage(), 2)
        self.canvas.itemconfig("oppcard", image = self.opp_selection_image)
        self.canvas.itemconfig("time", text = f"{self.turn_time}s")
        self.endTurn()

    def drawCard(self):
        index = 0
        for i in range(0, 6):
            if self.my_hand[i] == None:
                index = i
                break
        
        drawn = self.my_deck.pop(0)
        self.my_hand[index] = drawn
        self.hand_image_names[index] = drawn.getImage()
        self.updateHand("draw")

    def playCard(self, index):
        self.selected_card = self.my_hand[index]
        image_name = self.selected_card.getImage()
        self.selected_card_image = self.image_handler.resizeImage(image_name, 2)
        self.canvas.itemconfig("mycard", image = self.selected_card_image)
        self.my_hand[index] = None
        self.hand_image_names[index] = "noCard.jpg"
        self.updateHand("play")
    
    def endTurn(self):
        my_stat = self.selected_card.getStats()[self.checking]
        if self.selected_card.getTurnPower() == self.current_turn:
            bonus = self.selected_card.getBonusPower()
            my_stat += bonus
            self.canvas.itemconfig("feed", text = f"Turno de poder a favor activado +{bonus}")
            time.sleep(2)

        opp_stat = self.opp_selection.getStats()[self.checking]
        if self.opp_selection.getTurnPower() == self.current_turn:
            bonus = self.opp_selection.getBonusPower()
            opp_stat += bonus
            self.canvas.itemconfig("feed", text = f"Turno de poder en contra activado +{bonus}")
            time.sleep(2)

        self.canvas.itemconfig("feed", text = f"{my_stat} vs {opp_stat}")
        time.sleep(2)
        if  my_stat > opp_stat:
            self.canvas.itemconfig("feed", text = "Ganador del turno")
            self.wins += 1
        elif my_stat < opp_stat:
            self.canvas.itemconfig("feed", text = "Perdedor del turno")
            self.losses += 1
        else:
            chance = randint(1, 100)
            if chance % 2 == 0:
                self.canvas.itemconfig("feed", text = "Ganador del turno")
                self.wins += 1
            else:
                self.canvas.itemconfig("feed", text = "Perdedor del turno")
                self.losses += 1
        time.sleep(5)

        if self.wins > self.turns/2:
            self.canvas.itemconfig("feed", text = "Victoria")
            self.player.getWin()
            time.sleep(5)
            self.back()
        elif self.losses > self.turns/2:
            self.canvas.itemconfig("feed", text = "Derrota")
            time.sleep(5)
            self.back()
        else:
            self.selected_card = None
            self.selected_card_image = self.image_handler.resizeImage("noCard.jpg", 2)
            self.canvas.itemconfig("mycard", image = self.selected_card_image)

            self.opp_selection = None
            self.opp_selection_image = self.image_handler.resizeImage("noCard.jpg", 2)
            self.canvas.itemconfig("oppcard", image = self.opp_selection_image)
            self.startTurn()

    