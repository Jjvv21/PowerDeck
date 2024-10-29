import tkinter as tk
from tkinter import messagebox

from PlayerManager import *
from RegisterUI import *
from MainUI import *

class LogInUI:
    player_manager = PlayerManager()

    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 250, height = 150, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(80, 10, anchor = tk.NW, text = "Inicio de Sesión")

        self.canvas.create_text(20, 50, anchor = tk.NW, text = "Correo: ")
        self.mail_entry = tk.Entry(self.canvas, width = 20)
        self.mail_entry.place(x = 90, y = 50)

        self.canvas.create_text(20, 70, anchor = tk.NW, text = "Contraseña: ")
        self.password_entry = tk.Entry(self.canvas, show = "*", width = 20)
        self.password_entry.place(x = 90, y = 70)

        self.log_in_button = tk.Button(self.canvas, text = "Iniciar Sesión", command = self.logIn)
        self.log_in_button.place(x = 50, y = 100)

        self.to_album_button = tk.Button(self.canvas, text = "Registrarse", command = self.toRegisterUI)
        self.to_album_button.place(x = 150, y = 100)

    def logIn(self):
        mail = self.mail_entry.get()
        password = self.password_entry.get()

        if mail == "":
            messagebox.showerror("Error", "Introduzca un correo")
            return
        
        player_index = self.player_manager.exists(mail)
        if player_index < 0:
            messagebox.showerror("Error", f"No existe una cuenta con el correo {mail}")
            return
        player = self.player_manager.getPlayer(player_index)
        
        if password == "":
            messagebox.showerror("Error", "Introduzca la contraseña")
            return
        
        if not player.getPassword() == password:
            messagebox.showerror("Error", "Contraseña Incorrecta")
            return
        
        self.toMainUI(player)
    
    def toMainUI(self, player):
        self.window.withdraw()
        main_window = tk.Toplevel()
        main_window.title("PowerDeck")
        main_window.resizable(width = tk.NO, height = tk.NO)
        main_ui = MainUI(main_window, self, player)
        main_ui.run()

    def toRegisterUI(self):
        self.window.withdraw()
        register_window = tk.Toplevel()
        register_window.title("Registro")
        register_window.resizable(width = tk.NO, height = tk.NO)
        register_ui = RegisterUI(register_window, self, self.player_manager)
        register_ui.run()

    def run(self):
        self.window.mainloop()