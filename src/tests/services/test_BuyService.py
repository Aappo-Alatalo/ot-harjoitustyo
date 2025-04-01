import unittest
from services.BuyService import BuyService

class TestBuyService(unittest.TestCase):
    def setUp(self):
        self.buy_service = BuyService()

    def test_buy_stock(self):
        result = self.buy_service.buy_stock("AAPL", 5)
        self.assertEqual(result, "Purchased 5 shares of AAPL.")

