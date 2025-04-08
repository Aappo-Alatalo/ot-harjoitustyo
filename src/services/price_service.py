import yfinance as yf


class PriceService:
    def __init__(self, api_client=yf):
        self._api_client = api_client

    def get_stock_price(self, ticker):
        stock = self._api_client.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return price


price_service = PriceService()
