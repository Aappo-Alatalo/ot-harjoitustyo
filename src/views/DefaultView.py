from tkinter import ttk
from services.portfolio_service import PortfolioService
from services.price_service import price_service

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

        funds_label = ttk.Label(master=self._frame, text=f"Account balance: {self._portfolio_service.get_funds('Default'):.2f} €", font=('', 16))

        viewtitle = ttk.Label(master=self._frame,
                              text="This month overview", font=('', 32))
        
        portfolio_label = ttk.Label(master=self._frame, text="Your portfolio:", font=('', 14))

        table = ttk.Treeview(
            master=self._frame,
            columns=("Name", "Amount", "Value", "Valuation Change", "Sell"),
            show="headings"
        )

        table.heading("Name", text="Name")
        table.heading("Amount", text="Amount")
        table.heading("Value", text="Value")
        table.heading("Valuation Change", text="Valuation Change")
        table.heading("Sell", text="Sell")

        investments = self._portfolio_service.get_investments("Default")
        if investments:
            for investment in investments:
                current_price = price_service.get_stock_price(investment.name)
                table.insert(parent="", index=0, values=(investment.name, int(investment.amount), f"{(investment.amount * current_price):.2f} €", f"{(((current_price-investment.purchase_price)/investment.purchase_price) * 100):.2f}%" ,"Sell"))
        else:
            print("No investments found for this portfolio.")

        button = ttk.Button(
            master=self._frame,
            text="BUY",
            command=self._show_buy_view
        )

        funds_label.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")
        viewtitle.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
        portfolio_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        table.grid(row=3, column=0, padx=10, pady=5, sticky="NSEW")
        button.grid(row=4, column=0, padx=10, pady=3, sticky="ew")
