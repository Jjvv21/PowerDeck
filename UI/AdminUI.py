from logic.CardAlbum import *
from UI.CreateCardUI import *
from UI.AlbumUI import *
from UI.NewAdminUI import *

class AdminUI:
    album = CardAlbum()

    def __init__(self, window, caller, admin, admin_manager, player_manager):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        """
        self.admin = admin
        self.admin_manager = admin_manager
        self.player_manager = player_manager
        self.caller = caller
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 250, height = 250, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(50, 5, anchor = tk.NW, text = f"Administración de {self.admin.getRole()}")
        self.canvas.create_text(40, 25, anchor = tk.NW, text = f"Bienvenido {self.admin.getName()}")

        match self.admin.getRole():
            case "Juego":
                self.placeGameOptions()
            case "Control":
                self.placeControlOptions()

        self.new_admin_button = tk.Button(self.canvas, text = "Crear Administrador", command = self.toNewAdmin)
        self.new_admin_button.place(x = 10, y = 220)

        self.back_button = tk.Button(self.canvas, text = "Cerrar Sesión", command = self.back)
        self.back_button.place(x = 150, y = 220)

    def placeGameOptions(self):
        self.to_add_button = tk.Button(self.canvas, text = "Agregar Carta", command = self.toCardCreation)
        self.to_add_button.place(x = 10, y = 70)

        self.to_album_button = tk.Button(self.canvas, text = "Álbum", command = self.toAlbum)
        self.to_album_button.place(x = 130, y = 70)

        self.to_edit_button = tk.Button(self.canvas, text = "Editar Carta")
        self.to_edit_button.place(x = 30, y = 100)

        self.to_shop_button = tk.Button(self.canvas, text = "Productos de Tienda")
        self.to_shop_button.place(x = 10, y = 130)

        self.to_game_button = tk.Button(self.canvas, text = "Parámentros de Juego")
        self.to_game_button.place(x = 10, y = 160)

    def placeControlOptions(self):
        self.to_add_button = tk.Button(self.canvas, text = "Monitoreo")
        self.to_add_button.place(x = 10, y = 70)

        self.to_album_button = tk.Button(self.canvas, text = "Tienda")
        self.to_album_button.place(x = 130, y = 70)

        self.to_edit_button = tk.Button(self.canvas, text = "Transacciones de Venta")
        self.to_edit_button.place(x = 30, y = 100)

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

    def toNewAdmin(self):
        """
        toNewAdmin hides this UI and proceeds to the Admin Creation UI.
        """
        self.window.withdraw()
        new_admin_window = tk.Toplevel()
        new_admin_window.title("Creación de Administrador")
        new_admin_window.resizable(width = tk.NO, height = tk.NO)
        new_admin_ui = NewAdminUI(new_admin_window, self, self.admin_manager, self.player_manager)
        new_admin_ui.run()
    
    def run(self):
        """
        run runs the main loop of the UI.
        """
        self.window.mainloop()

    def back(self):
        """
        back returns to the UI that called this one.
        """
        self.window.destroy()
        self.caller.window.deiconify()