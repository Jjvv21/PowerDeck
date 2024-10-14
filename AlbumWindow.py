from tkinter import *
from tkinter import messagebox

from functions import loadImage

class AlbumWindow:
    selected_card = 0
    img = "noImage.jpg"
    filtering = False
    main_cards = []

    def __init__(self, window, caller):
        self.caller = caller
        self.window = window
        self.canvas = Canvas(self.window, width = 800, height = 600)
        self.canvas.pack()

        self.scroll = Scrollbar(self.canvas)
        self.scroll.place(height = 700, x = 170, y = 50)
        self.listbox = Listbox(self.canvas, height = 30, width = 62, yscrollcommand = self.scroll.set)
        self.listbox.place(x = 1, y = 50)
        self.scroll.config(command = self.listbox.yview)

        if len(self.caller.cards) > 0:
            for i in self.caller.cards:
                name = i.getName() + ", " + i.getVarName()
                self.listbox.insert(END, name)
                main = i.isMain()
                if main:
                    self.main_cards.append(i)
        else:
            messagebox.showerror("Error", "No existen cartas creadas")

        posX = 450
        self.canvas.create_text(posX, 50, anchor = NW, text = "Nombre: ")
        self.name_entry = Entry(self.canvas, width = 30, state = "readonly")
        self.name_entry.place(x = posX + 60, y = 50)

        self.canvas.create_text(posX, 70, anchor = NW, text = "Variante: ")
        self.var_entry = Entry(self.canvas, width = 30, state = "readonly")
        self.var_entry.place(x = posX + 60, y = 70)

        self.canvas.create_text(posX, 90, anchor = NW, text = "Raza: ")
        self.race_entry = Entry(self.canvas, width = 10, state = "readonly")
        self.race_entry.place(x = posX + 60, y = 90)

        self.canvas.create_text(posX, 110, anchor = NW, text = "Rareza: ")
        self.rarity_entry = Entry(self.canvas, width = 10, state = "readonly")
        self.rarity_entry.place(x = posX + 60, y = 110)

        self.canvas.create_text(posX, 130, anchor = NW, text = "Activa en Juego: ")
        self.game_active_entry = Entry(self.canvas, width = 2, state = "readonly")
        self.game_active_entry.place(x = posX + 100, y = 130)

        self.canvas.create_text(posX, 150, anchor = NW, text = "Activa en Sobres: ")
        self.pull_active_entry = Entry(self.canvas, width = 2, state = "readonly")
        self.pull_active_entry.place(x = posX + 100, y = 150)

        self.canvas.create_text(posX, 170, anchor = NW, text = "Llave: ")
        self.key_entry = Entry(self.canvas, width = 30, state = "readonly")
        self.key_entry.place(x = posX + 60, y = 170)

        self.canvas.create_text(posX, 190, anchor = NW, text = "Fecha de Modificación: ")
        self.mod_date_entry = Entry(self.canvas, width = 10, state = "readonly")
        self.mod_date_entry.place(x = posX + 140, y = 190)

        self.selected_img = loadImage(self.img)
        self.canvas.create_image(posX + 10, 220, anchor = NW, image = self.selected_img, tags = "card_img")

        self.show_button = Button(self.canvas, text = "Mostrar", command = self.selectCard)
        self.show_button.place(x = 540, y = 560)

        self.filter_main_button = Button(self.canvas, text = "Filtrar Principales", command = self.showMain)
        self.filter_main_button.place(x = 50, y = 540)

        self.show_all_button = Button(self.canvas, text = "Ver todas las cartas", command = self.showAll, state = DISABLED)
        self.show_all_button.place(x = 50, y = 570)

        self.back_button = Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 740, y = 570)

    def run(self):
        self.window.mainloop()

    def showSelection(self):
        if not self.filtering:
            card = self.caller.cards[self.selected_card]
        else:
            card = self.main_cards[self.selected_card]

        self.name_entry.config(state = "normal")
        self.name_entry.delete(0, END)
        self.name_entry.insert(0, card.getName())
        self.name_entry.config(state = "readonly")

        self.var_entry.config(state = "normal")
        self.var_entry.delete(0, END)
        self.var_entry.insert(0, card.getVarName())
        self.var_entry.config(state = "readonly")

        self.race_entry.config(state = "normal")
        self.race_entry.delete(0, END)
        self.race_entry.insert(0, card.getRace())
        self.race_entry.config(state = "readonly")

        self.rarity_entry.config(state = "normal")
        self.rarity_entry.delete(0, END)
        self.rarity_entry.insert(0, card.getRarity())
        self.rarity_entry.config(state = "readonly")

        self.game_active_entry.config(state = "normal")
        self.game_active_entry.delete(0, END)
        if card.gameActive():
            str_game_active = "Sí"
        else:
            str_game_active = "No"
        self.game_active_entry.insert(0, str_game_active)
        self.game_active_entry.config(state = "readonly")

        self.pull_active_entry.config(state = "normal")
        self.pull_active_entry.delete(0, END)
        if card.pullActive():
            str_pull_active = "Sí"
        else:
            str_pull_active = "No"
        self.pull_active_entry.insert(0, str_pull_active)
        self.pull_active_entry.config(state = "readonly")

        self.key_entry.config(state = "normal")
        self.key_entry.delete(0, END)
        self.key_entry.insert(0, card.getID())
        self.key_entry.config(state = "readonly")

        self.mod_date_entry.config(state = "normal")
        self.mod_date_entry.delete(0, END)
        self.mod_date_entry.insert(0, card.lastMod())
        self.mod_date_entry.config(state = "readonly")

        self.selected_img = loadImage(card.getImage())
        self.canvas.itemconfig("card_img", image = self.selected_img)

    def selectCard(self):
        try:
            self.selected_card = self.listbox.curselection()[0]
            self.showSelection()
        except:
            messagebox.showerror("Error", "Seleccione una Carta para mostrar")

    def showMain(self):
        if len(self.main_cards) > 0:
            self.listbox.delete(0, END)
            self.filtering = True
            for i in self.main_cards:
                name = i.getName() + ", " + i.getVarName()
                self.listbox.insert(END, name)
            self.filter_main_button.config(state = DISABLED)
            self.show_all_button.config(state = NORMAL)
        else:
            messagebox.showerror("Error", "No existen cartas para filtrar")

    def showAll(self):
        self.listbox.delete(0 , END)
        self.filtering = False
        for i in self.caller.cards:
            name = i.getName() + ", " + i.getVarName()
            self.listbox.insert(END, name)
        self.show_all_button.config(state = DISABLED)
        self.filter_main_button.config(state = NORMAL)

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()