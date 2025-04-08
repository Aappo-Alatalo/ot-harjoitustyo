import unittest

from db.build import build
from db.database_connection import get_database_connection

from repositories.portfolio_repository import PortfolioRepository
from entities.investment import Investment


class TestPortfolioRepository(unittest.TestCase):
    def setUp(self):
        build()
        self.connection = get_database_connection()
        self.portfolio_repository = PortfolioRepository(self.connection)
        self.portfolio_repository.clear()

    def test_save_investment(self):
        investment_id = self.portfolio_repository.save(
            "stock", "AAPL", 10, 150.0)
        self.assertIsNotNone(investment_id)

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM investments WHERE id = ?",
                       (investment_id,))
        row = cursor.fetchone()

        self.assertIsNotNone(row)
        self.assertEqual(row["type"], "stock")
        self.assertEqual(row["name"], "AAPL")
        self.assertEqual(row["amount"], 10)
        self.assertEqual(row["purchase_price"], 150.0)

    def test_get_all_investments(self):
        self.portfolio_repository.save("stock", "AAPL", 10, 150.0)
        self.portfolio_repository.save("stock", "SBUX", 2, 80.0)

        investments = self.portfolio_repository.get_all()

        self.assertEqual(len(investments), 2)
        self.assertIsInstance(investments[0], Investment)
        self.assertEqual(investments[0].name, "AAPL")
        self.assertEqual(investments[1].name, "SBUX")
