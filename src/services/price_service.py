import yfinance as yf


class PriceService:
    def __init__(self, api_client=yf):
        self._api_client = api_client

    def get_stock_price(self, ticker):

        if not ticker:
            raise ValueError("Ticker cannot be empty")
        if not isinstance(ticker, str):
            raise TypeError("Ticker must be a string")

        try:
            stock = self._api_client.Ticker(ticker)
            price = stock.history(period="1d")["Close"].iloc[-1]
        except:
            print(f"Error retrieving price for {ticker}.")
            return None

        return price


price_service = PriceService()
