from CardAlbum import *
from CreateCardUI import *
from AlbumUI import *

class AdminUI:
    album = CardAlbum()

    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 250, height = 150, bg = "#78a090")
        self.canvas.pack()

        self.to_add_button = tk.Button(self.canvas, text = "Agregar Carta", command = self.openAdd)
        self.to_add_button.place(x = 50, y = 70)

        self.to_album_button = tk.Button(self.canvas, text = "Álbum", command = self.openAlbum)
        self.to_album_button.place(x = 150, y = 70)

    def run(self):
        self.window.mainloop()

    def openAdd(self):
        self.window.withdraw()
        window_add = tk.Toplevel()
        window_add.title("Creación de Cartas")
        window_add.resizable(width = tk.NO, height = tk.NO)
        add = CreateCardUI(window_add, self, self.album)
        add.run()

    def openAlbum(self):
        self.window.withdraw()
        window_album = tk.Toplevel()
        window_album.title("Álbum de Cartas")
        window_album.resizable(width = tk.NO, height = tk.NO)
        album = AlbumUI(window_album, self, self.album.getCards())
        album.run()
