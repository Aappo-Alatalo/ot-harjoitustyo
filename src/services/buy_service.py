from repositories.investment_repository import (
    investment_repository as default_investment_repo,
)
from services.price_service import (
    price_service as default_price_service,
)
from services.portfolio_service import (
    portfolio_service as default_portfolio_service,
)


class BuyService:
    def __init__(self,
                 price_service=default_price_service,
                 investment_repo=default_investment_repo,
                 portfolio_service=default_portfolio_service):

        self._portfolio_service = portfolio_service
        self._price_service = price_service
        self._investment_repo = investment_repo

    def buy_stock(self, ticker, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if not isinstance(ticker, str):
            raise TypeError("Ticker must be a string")
        if not ticker:
            raise ValueError("Ticker cannot be empty")

        print(f"Buying {amount} shares of {ticker}...")
        price = self._price_service.get_stock_price(ticker)
        if price is None:
            raise ValueError(f"Could not retrieve price for {ticker}")

        if price * amount > self._portfolio_service.get_funds("Default"):
            return print("Not enough funds")

        try:
            self._investment_repo.save(1, "stock", ticker, amount, price)
        except:
            return print("Failed to save investment")

        try:
            self._portfolio_service.subtract_funds(
                "Default", price * amount)
        except:
            return print("Failed to subtract funds")

        print(
            f"Successfully bought {amount} shares of {ticker} at {price} each.")
        return True
