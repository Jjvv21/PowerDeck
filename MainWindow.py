import pickle

from AddWindow import *
from AlbumWindow import *

class MainWindow:
    cards = []

    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(self.window, width = 500, height = 500)
        self.canvas.pack()

        try:
            self.loadCards()
        except:
            print("no cards found")

        self.to_add_button = Button(self.canvas, text = "Agregar Carta", command = self.openAdd)
        self.to_add_button.place(x = 10, y = 390)

        self.to_album_button = Button(self.canvas, text = "álbum", command = self.openAlbum)
        self.to_album_button.place(x = 100, y = 390)

    def run(self):
        self.window.mainloop()

    def loadCards(self):
        file = open("cards.txt", "rb")
        self.cards.extend(pickle.load(file))
        file.close()
        print("cards loaded")

    def saveCards(self):
        file = open("cards.txt", "wb")
        pickle.dump(self.cards, file)
        file.close()
        print("cards saved")

    def sortCards(self):
        order = []
        for i in self.cards:
            name = i.getName().lower()
            var = i.getVarName().lower()
            order.append(name + var)
        order.sort()

        sorted_cards = []
        for j in range(0, len(order)):
            for k in self.cards:
                name = k.getName().lower()
                var = k.getVarName().lower()
                if (name + var) == order[j]:
                    sorted_cards.append(k)

        self.cards = sorted_cards
        self.saveCards()

    def openAdd(self):
        self.window.withdraw()
        window_add = Toplevel()
        window_add.title("Creación de Cartas")
        window_add.resizable(width = NO, height = NO)
        add = AddWindow(window_add, self)
        add.run()

    def openAlbum(self):
        self.window.withdraw()
        window_album = Toplevel()
        window_album.title("Álbum de Cartas")
        window_album.resizable(width = NO, height = NO)
        album = AlbumWindow(window_album, self)
        album.run()

