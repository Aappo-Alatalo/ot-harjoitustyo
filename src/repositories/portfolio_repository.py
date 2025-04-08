from db.database_connection import get_database_connection as get_default_db
from entities.investment import Investment


class PortfolioRepository:
    def __init__(self, connection=get_default_db()):
        self._connection = connection

    def save(self, investment_type, ticker, amount, price):
        cursor = self._connection.cursor()

        cursor.execute('''
            INSERT INTO investments (type, name, amount, purchase_price)
            VALUES (?, ?, ?, ?)
        ''', (investment_type, ticker, amount, price))

        self._connection.commit()
        print("Investment saved successfully.")
        return cursor.lastrowid

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM investments")

        rows = cursor.fetchall()

        return [
            Investment(
                row["id"],
                row["type"],
                row["name"],
                row["amount"],
                row["purchase_price"]
            )
            for row in rows
        ]


portfolio_repository = PortfolioRepository()
