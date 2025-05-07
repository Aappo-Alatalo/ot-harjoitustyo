import unittest
from unittest.mock import MagicMock
from services.buy_service import BuyService


class TestBuyService(unittest.TestCase):
    def setUp(self):
        self.mock_price_service = MagicMock()
        self.mock_investment_repo = MagicMock()
        self.buy_service = BuyService(
            price_service=self.mock_price_service,
            investment_repo=self.mock_investment_repo,
        )

    def test_buy_stock(self):
        self.mock_price_service.get_stock_price.return_value = 150
        self.buy_service.buy_stock("AAPL", 5)
        self.mock_price_service.get_stock_price.assert_called_once_with("AAPL")
        self.mock_investment_repo.save.assert_called_once_with(
            "stock", "AAPL", 5, 150)
