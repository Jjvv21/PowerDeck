from CardAlbum import *
from AddWindow import *
from AlbumWindow import *

class MainWindow:
    album = CardAlbum()

    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 500, height = 500)
        self.canvas.pack()

        try:
            self.album.load()
        except:
            print("no cards found")

        self.to_add_button = tk.Button(self.canvas, text = "Agregar Carta", command = self.openAdd)
        self.to_add_button.place(x = 10, y = 390)

        self.to_album_button = tk.Button(self.canvas, text = "álbum", command = self.openAlbum)
        self.to_album_button.place(x = 100, y = 390)

    def run(self):
        self.window.mainloop()

    def openAdd(self):
        self.window.withdraw()
        window_add = tk.Toplevel()
        window_add.title("Creación de Cartas")
        window_add.resizable(width = tk.NO, height = tk.NO)
        add = AddWindow(window_add, self, self.album)
        add.run()

    def openAlbum(self):
        self.window.withdraw()
        window_album = tk.Toplevel()
        window_album.title("Álbum de Cartas")
        window_album.resizable(width = tk.NO, height = tk.NO)
        album = AlbumWindow(window_album, self, self.album.getCards())
        album.run()

