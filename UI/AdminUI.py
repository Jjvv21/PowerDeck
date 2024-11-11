from logic.CardAlbum import *
from UI.CreateCardUI import *
from UI.AlbumUI import *

class AdminUI:
    album = CardAlbum()

    def __init__(self, window):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        """
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 250, height = 150, bg = "#78a090")
        self.canvas.pack()

        self.to_add_button = tk.Button(self.canvas, text = "Agregar Carta", command = self.toCardCreation)
        self.to_add_button.place(x = 50, y = 70)

        self.to_album_button = tk.Button(self.canvas, text = "Álbum", command = self.toAlbum)
        self.to_album_button.place(x = 150, y = 70)    

    def toCardCreation(self):
        """
        toCradCreation hides this UI and proceeds to the Card Creation UI.
        """
        self.window.withdraw()
        create_card_window = tk.Toplevel()
        create_card_window.title("Creación de Cartas")
        create_card_window.resizable(width = tk.NO, height = tk.NO)
        add = CreateCardUI(create_card_window, self, self.album)
        add.run()

    def toAlbum(self):
        """
        toAlbum hides this UI and proceeds to the Card Album UI.
        """
        self.window.withdraw()
        album_window = tk.Toplevel()
        album_window.title("Álbum de Cartas")
        album_window.resizable(width = tk.NO, height = tk.NO)
        album = AlbumUI(album_window, self, self.album.getCards())
        album.run()
    
    def run(self):
        """
        run runs the main loop of the UI.
        """
        self.window.mainloop()