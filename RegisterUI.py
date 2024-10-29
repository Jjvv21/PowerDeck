import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from ImageHandler import *

class RegisterUI:
    countries = ["Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda",
                 "Arabia Saudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria",
                 "Azerbaiyán", "Bahamas", "Bahrein", "Bangladesh", "Barbados", "Belarús", "Bélgica",
                 "Belice", "Benin", "Bhután", "Bolivia", "Bosnia y Herzegovina", "Botswana",
                 "Brasil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Camboya",
                 "Camerún", "Canadá", "Chad", "Chile", "China", "Chipre", "Colombia", "Comoras",
                 "Congo", "Costa Rica"]
    image_name = "noImage.jpg"
    path = ""
    img_handler = ImageHandler()

    def __init__(self, window, caller, player_manager):
        self.caller = caller
        self.player_manager = player_manager
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 550, height = 400)
        self.canvas.pack()

        self.canvas.create_text(10, 50, anchor = tk.NW, text = "Nombre: ")
        self.name_entry = tk.Entry(self.canvas, width = 30)
        self.name_entry.place(x = 60, y = 50)   
        self.name_entry.bind('<KeyPress>', self.nameCharCount)
        self.name_entry.bind('<KeyRelease>', self.nameCharCount)     

        self.canvas.create_text(10, 70, anchor = tk.NW, text = "Alias: ")
        self.username_entry = tk.Entry(self.canvas, width = 30)
        self.username_entry.place(x = 60, y = 70)
        self.username_entry.bind('<KeyPress>', self.usernameCharCount)
        self.username_entry.bind('<KeyRelease>', self.usernameCharCount) 

        self.canvas.create_text(10, 90, anchor = tk.NW, text = "Contraseña: ")
        self.password_entry = tk.Entry(self.canvas, width = 8)
        self.password_entry.place(x = 150, y = 90)   
        self.password_entry.bind('<KeyPress>', self.passwordCharCount)
        self.password_entry.bind('<KeyRelease>', self.passwordCharCount) 

        self.canvas.create_text(10, 110, anchor = tk.NW, text = "Confirmar Contraseña: ")
        self.confirm_password_entry = tk.Entry(self.canvas, width = 8)
        self.confirm_password_entry.place(x = 150, y = 110)   
        self.confirm_password_entry.bind('<KeyPress>', self.confirmCharCount)
        self.confirm_password_entry.bind('<KeyRelease>', self.confirmCharCount)

        self.canvas.create_text(10, 130, anchor = tk.NW, text = "Correo: ")
        self.mail_entry = tk.Entry(self.canvas, width = 30)
        self.mail_entry.place(x = 60, y = 130)

        self.canvas.create_text(10, 150, anchor = tk.NW, text = "País: ")
        self.country_combo = ttk.Combobox(self.canvas, state = "readonly",values = self.countries, width = 20)
        self.country_combo.place(x = 60, y = 150)

        self.selected_img = self.img_handler.loadImage("noImage.jpg")
        self.canvas.create_image(250, 80, anchor = tk.NW, image = self.selected_img, tags = "selection")

        self.select_img_button = tk.Button(self.canvas, text = "Seleccionar Imagen", command = self.getImage)
        self.select_img_button.place(x = 300, y = 50)

        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 490, y = 370)

    def nameCharCount(self, event):
        count = len(self.name_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def usernameCharCount(self, event):
        count = len(self.username_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def passwordCharCount(self, event):
        count = len(self.password_entry.get())
        if count >= 8 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'

    def confirmCharCount(self, event):
        count = len(self.confirm_password_entry.get())
        if count >= 8 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def getImage(self):
        self.path = filedialog.askopenfilename()
        isImage = self.img_handler.checkImage(self.path)
        match isImage:
            case -1:
                return
            case -2:
                messagebox.showerror("Error", "Seleccione una archivo .png o .jpg")
                self.path = ""
            case -3:
                messagebox.showerror("Error", "Tamaño de imagen incorrecto")
                self.path = ""
            case _:
                self.selected_img = self.img_handler.loadExternalImage(self.path)
                self.canvas.itemconfig("selection", image = self.selected_img)
                self.image_name = self.path[-isImage]
                messagebox.showinfo("Éxito", "Imagen cargada")

    def createPlayer(self):
        name = self.name_entry.get()
        username = self.username_entry.get()

        password = self.password_entry.get()
        password_confirmation = self.confirm_password_entry.get()
        if password != password_confirmation:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        mail = self.mail_entry.get()
        country = self.country_combo.get()
        image = self.image_name

        result = self.player_manager.add(name, username, password, mail, country, image)
        match result:
            case 0:
                messagebox.showinfo("Éxito", f"Jugador {username} creado")
                self.back()
            case -1:
                messagebox.showerror("Error", "El nombre debe tener entre 5 y 30 caracteres")
            case -2:
                messagebox.showerror("Error", "El alias debe tener entre 5 y 30 caracteres")
            case -3:
                messagebox.showerror("Error", "Ingrese un correo")
            case -4:
                messagebox.showerror("Error", "El alias ya existe")
            case -5:
                messagebox.showerror("Error", "El correo ya se encuentra en uso")
            case -6:
                messagebox.showerror("Error", "Ingrese una contraseña entre 6 y 8 caracteres")
            case -7:
                messagebox.showerror("Error", "Contraseña inválida, debe ser alfanumérica")
            case -8:
                messagebox.showerror("Error", "Seleccione un país")
        
    def run(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()