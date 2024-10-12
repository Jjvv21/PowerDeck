from AddWindow import *

class MainWindow:
    cards = []

    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(self.window, width = 500, height = 500)
        self.canvas.pack()

        self.SettingsButton = Button(self.canvas, text = "Agregar Carta", command = self.openAdd)
        self.SettingsButton.place(x = 10, y = 390)

    def run(self):
        self.window.mainloop()

    def openAdd(self):
        self.window.withdraw()
        windowAdd = Toplevel()
        windowAdd.title("Creación de Cartas")
        windowAdd.resizable(width = NO, height = NO)
        add = AddWindow(windowAdd, self)
        add.run()

