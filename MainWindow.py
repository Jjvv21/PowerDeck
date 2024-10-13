import pickle

from AddWindow import *

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

    def openAdd(self):
        self.window.withdraw()
        window_add = Toplevel()
        window_add.title("Creación de Cartas")
        window_add.resizable(width = NO, height = NO)
        add = AddWindow(window_add, self)
        add.run()

