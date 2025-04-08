import unittest
from unittest.mock import MagicMock
from services.price_service import PriceService
import pandas as pd


class TestPriceService(unittest.TestCase):
    def setUp(self):
        self.mock_api_client = MagicMock()
        self.price_service = PriceService(api_client=self.mock_api_client)

    def test_get_stock_price(self):
        mock_ticker = MagicMock()

        mock_history = {"Close": pd.Series([100.0])}
        mock_ticker.history.return_value = mock_history
        self.mock_api_client.Ticker.return_value = mock_ticker

        price = self.price_service.get_stock_price("AAPL")

        self.mock_api_client.Ticker.assert_called_once_with("AAPL")
        mock_ticker.history.assert_called_once_with(period="1d")
        self.assertEqual(price, 100.0)
