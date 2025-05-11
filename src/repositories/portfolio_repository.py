from db.database_connection import get_database_connection as get_default_db
from entities.portfolio import Portfolio
from entities.investment import Investment


class PortfolioRepository:
    def __init__(self, connection=get_default_db()):
        self._connection = connection

    def add_funds(self, name, amount):
        cursor = self._connection.cursor()

        cursor.execute('''
            UPDATE portfolio
            SET funds = funds + ?
            WHERE name = ?
        ''', (amount, name))

        self._connection.commit()
        print("Portfolio funds added successfully.")
        return cursor.lastrowid
    
    def subtract_funds(self, name, amount):
        cursor = self._connection.cursor()

        cursor.execute('''
            UPDATE portfolio
            SET funds = funds - ?
            WHERE name = ?
        ''', (amount, name))
        
        self._connection.commit()
        print("Portfolio funds subtracted successfully.")
        return cursor.lastrowid
    
    def get(self, name):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM portfolio WHERE name = ?", (name,))

        row = cursor.fetchone()

        if row:
            return Portfolio(
                row["id"],
                row["name"],
                row["funds"],
            )
        else:
            return None

    def get_investments(self, name):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM investment WHERE portfolio_id = (SELECT id FROM portfolio WHERE name = ?)", (name,))

        rows = cursor.fetchall()

        investments = []
        for row in rows:
            investments.append(
                Investment(
                    row["id"],
                    row["type"],
                    row["name"],
                    row["amount"],
                    row["purchase_price"]
                )
            )

        return investments 

portfolio_repository = PortfolioRepository()
