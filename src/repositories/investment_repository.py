from db.database_connection import get_database_connection as get_default_db
from entities.investment import Investment


class InvestmentRepository:
    def __init__(self, connection=get_default_db()):
        self._connection = connection

    def save(self, portfolio_id, investment_type, ticker, amount, price):
        if not portfolio_id or not investment_type or not ticker or not amount or not price:
            raise ValueError("Required fields are missing")

        if not isinstance(portfolio_id, int):
            raise TypeError("Portfolio ID must be an integer")
        if not isinstance(investment_type, str):
            raise TypeError("Investment type must be a string")
        if not isinstance(ticker, str):
            raise TypeError("Ticker must be a string")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT id, amount, purchase_price FROM investment
            WHERE portfolio_id = ? AND name = ?
        ''', (portfolio_id, ticker))
        
        existing = cursor.fetchone()
        if existing:
            existing_amount = existing["amount"]
            existing_price = existing["purchase_price"]

            total_amount = existing_amount + amount
            new_avg_price = ((existing_amount * existing_price) + (amount * price)) / total_amount
            cursor.execute('''
                UPDATE investment
                SET amount = ?, purchase_price = ?
                WHERE id = ?
            ''', (total_amount, new_avg_price, existing["id"]))
        else:
            cursor.execute('''
                INSERT INTO investment (portfolio_id, type, name, amount, purchase_price)
                VALUES (?, ?, ?, ?, ?)
            ''', (portfolio_id, investment_type, ticker, amount, price))

        self._connection.commit() 
        print("Investment saved successfully.")
        return cursor.lastrowid

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM investment")

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

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM investment")
        self._connection.commit()


investment_repository = InvestmentRepository()
