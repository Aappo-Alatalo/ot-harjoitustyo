from repositories.portfolio_repository import (
    portfolio_repository as default_portfolio_repo,
)
from services.price_service import (
    price_service as default_price_service,
)


class BuyService:
    def __init__(self, price_service=default_price_service, portfolio_repo=default_portfolio_repo):
        self._price_service = price_service
        self._portfolio_repo = portfolio_repo

    def buy_stock(self, ticker, amount):
        print(f"Buying {amount} shares of {ticker}...")
        price = self._price_service.get_stock_price(ticker)
        self._portfolio_repo.save("stock", ticker, amount, price)

