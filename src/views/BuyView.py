from tkinter import ttk, StringVar
from services.price_service import PriceService


class BuyView:
    def __init__(self, root, show_default_view, show_buy_stock_view):
        self._root = root
        self._show_default_view = show_default_view
        self._show_buy_stock_view = show_buy_stock_view
        self._frame = None
        self._price_service = PriceService()

        self._ticker_var = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _search(self):
        ticker = self._ticker_var.get().strip().upper()
        if ticker:
            try:
                price = self._price_service.get_stock_price(ticker)
                self._show_buy_stock_view(ticker, price)
            except Exception:
                self._show_buy_stock_view(ticker, None)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        viewtitle = ttk.Label(master=self._frame, text="BUY", font=('', 32))
        label = ttk.Label(master=self._frame,
                          text="Stocks/Crypto (search crypto:ticker-EUR)")
        ticker_entry = ttk.Entry(
            master=self._frame, textvariable=self._ticker_var)
        search_button = ttk.Button(
            master=self._frame,
            text="Search",
            command=self._search
        )
        back_button = ttk.Button(
            master=self._frame,
            text="back",
            command=self._show_default_view
        )

        back_button.grid(row=0, column=0, padx=10, pady=3, sticky="ew")
        viewtitle.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
        label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        ticker_entry.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        search_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
