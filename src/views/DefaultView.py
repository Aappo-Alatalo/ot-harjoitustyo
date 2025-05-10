from tkinter import ttk
from services.portfolio_service import PortfolioService

class DefaultView:
    def __init__(self, root, show_buy_view):
        self._root = root
        self._show_buy_view = show_buy_view
        self._frame = None
        
        self._portfolio_service = PortfolioService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        funds_label = ttk.Label(master=self._frame, text=f"Account balance: {self._portfolio_service.get_funds('Default'):.2f} €")

        viewtitle = ttk.Label(master=self._frame,
                              text="This month overview", font=('', 32))
        holdings_label = ttk.Label(master=self._frame, text="holdings")
        button = ttk.Button(
            master=self._frame,
            text="BUY",
            command=self._show_buy_view
        )

        funds_label.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")
        viewtitle.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
        holdings_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        button.grid(row=4, column=0, padx=10, pady=3, sticky="ew")
