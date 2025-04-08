from tkinter import ttk
from services.buy_service import BuyService


class BuyStockView:
    def __init__(self, root, show_buy_view, ticker, price):
        self._root = root
        self._show_buy_view = show_buy_view
        self._frame = None
        self._buy_service = BuyService()

        self._ticker = ticker
        self._price = price if price is not None else "N/A"

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _buy_stock(self):
        if self._price != "N/A":
            self._buy_service.buy_stock(self._ticker, 1)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        stock_name = ttk.Label(
            master=self._frame, text=self._ticker, font=('', 48))
        price = ttk.Label(
            master=self._frame, text=f"${self._price:.2f}" if self._price != "N/A" else "Price not available")
        buy_button = ttk.Button(
            master=self._frame,
            text="BUY",
            command=self._buy_stock
        )
        back_button = ttk.Button(
            master=self._frame,
            text="back",
            command=self._show_buy_view
        )

        back_button.grid(row=0, column=0, padx=10, pady=3, sticky="ew")
        stock_name.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
        price.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        buy_button.grid(row=3, column=0, padx=10, pady=3, sticky="ew")
