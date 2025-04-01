from tkinter import Tk
from views.DefaultView import DefaultView
from views.BuyView import BuyView
from views.BuyStockView import BuyStockView

class App:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_default_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _show_default_view(self):
        self._hide_current_view()

        self._current_view = DefaultView(
            self._root,
            self._show_buy_view
        )
        self._current_view.pack()

    def _show_buy_view(self):
        self._hide_current_view()

        self._current_view = BuyView(
            self._root,
            self._show_default_view,
            self._show_buy_stock_view
        )
        self._current_view.pack()

    def _show_buy_stock_view(self):
        self._hide_current_view()

        self._current_view = BuyStockView(
            self._root,
            self._show_buy_view
        )
        self._current_view.pack()

window = Tk()
window.title("Trade Royale")
window.geometry("800x600")

app = App(window)
app.start()

window.mainloop()
