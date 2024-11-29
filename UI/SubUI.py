from UI.TopUI import *

class SubUI(TopUI):

    def __init__(self, window, caller, width, height):
        """
        Constructor that intializes and places the widgets of the UI with a button for going back.

        :window: Toplevel container for the widgets.
        :caller: UI that called this one.
        :width: width for the window.
        :height: height for the window.
        """
        TopUI.__init__(self, window, width, height)
        self.caller = caller

        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = self.width - 60, y = self.height - 30)

    def back(self):
        """
        back returns to the UI that called this one.
        """
        self.window.destroy()
        self.caller.window.deiconify()