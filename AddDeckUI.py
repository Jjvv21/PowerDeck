import tkinter as tk
from tkinter import messagebox

from DeckBuilder import *
class AddDeckUI:
    deck_builder = DeckBuilder()
    cards = []
    decks = []

    def __init__(self, window, caller, player_manager, player):
        self.caller = caller
        self.player_manager = player_manager
        self.player = player
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 800, height = 600, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(10, 50, anchor = tk.NW, text = "Nombre: ")
        self.name_entry = tk.Entry(self.canvas, width = 30)
        self.name_entry.place(x = 60, y = 50)
        self.name_entry.bind('<KeyPress>', self.nameCharCount)
        self.name_entry.bind('<KeyRelease>', self.nameCharCount) 

        self.canvas.create_text(10, 70, anchor = tk.NW, text = "Cartas Disponibles:")
        self.cards_scroll = tk.Scrollbar(self.canvas)
        self.cards_scroll.place(height = 484, x = 420, y = 90)
        self.cards_listbox = tk.Listbox(self.canvas, selectmode = "multiple", height = 30, width = 75, yscrollcommand = self.cards_scroll.set)
        self.cards_listbox.place(x = 9, y = 90)
        self.cards_scroll.config(command = self.cards_listbox.yview)
        
        self.cards = player.showCards()
        if len(self.cards) > 0:
            for i in self.cards:
                name = i.getName() + ", " + i.getVariantName() + f" ({i.getRarity()})"
                self.cards_listbox.insert(tk.END, name)
            self.cards_listbox.selection_set(0)

        self.canvas.create_text(550, 70, anchor = tk.NW, text = "Decks Disponibles:")
        self.decks_listbox = tk.Listbox(self.canvas, height = 15, width = 30)
        self.decks_listbox.place(x = 549, y = 90)

        self.updateDecks()

        self.create_button = tk.Button(self.canvas, text = "Crear Deck", command = self.createDeck)
        self.create_button.place(x = 200, y = 575)

        self.show_button = tk.Button(self.canvas, text = "Ver Deck", command = self.showDeck)
        self.show_button.place(x = 600, y = 400)

        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 740, y = 570)

    def nameCharCount(self, event):
        count = len(self.name_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def createDeck(self):
        name = self.name_entry.get()
        if len(name) < 5:
            messagebox.showerror("Error", f"Introduzca un nombre para el deck entre 5 y 30 caracteres")
            return

        cards_indexes = self.cards_listbox.curselection()
        max_cards = self.deck_builder.getMaxCards()
        if len(cards_indexes) != max_cards[0]:
            messagebox.showerror("Error", f"Un deck debe tener exactamente {max_cards[0]} cartas")
            return
        
        selected_cards = []
        for i in cards_indexes:
            selected_cards.append(self.cards[i])

        result = self.deck_builder.createDeck(self.player, name, selected_cards)
        match result:
            case -1:        
                messagebox.showerror("Error", "No hay espacio para un nuevo Deck")
                return
            case -2:        
                messagebox.showerror("Error", "No pueden existir dos cartas repetidas")
                return
            case -3:        
                messagebox.showerror("Error", "Demasiadas cartas Ultra-Raras")
                return
            case -4:        
                messagebox.showerror("Error", "Demasiadas cartas Muy Raras")
                return
            case -5:        
                messagebox.showerror("Error", "Demasiadas cartas Raras")
                return
            case -6:        
                messagebox.showerror("Error", "Demasiadas cartas Normales")
                return
            case -7:        
                messagebox.showerror("Error", "Demasiadas carta Básicas")
                return
            case _:        
                messagebox.showinfo("Éxito", "Deck creado")
                self.updateDecks()
                self.player_manager.save()
                return
            
    def updateDecks(self):
        self.decks = self.player.showDecks()
        self.decks_listbox.delete(0, tk.END)
        if len(self.decks) > 0:
            for i in self.decks:
                name = i.getName()
                self.decks_listbox.insert(tk.END, name)
            self.decks_listbox.selection_set(0)

    def showDeck(self):
        if len(self.decks) > 0:
            selection = self.decks_listbox.curselection()[0]
            deck = self.decks[selection]
            valid = ""
            if deck.isValid():
                valid = "Válido"
            else:
                valid = "Inválido"
            cards = deck.getCards()
            cards_str = "Cartas:"
            for i in cards:
                cards_str += "\n - "
                cards_str += i.getName()
                cards_str += ", "
                cards_str += i.getVariantName()
            messagebox.showinfo("Deck", f"{deck.getName()}:\n \n" + cards_str + f"\n \nFecha de creación: {deck.getCreationDate()}\n" + valid)

    def run(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()