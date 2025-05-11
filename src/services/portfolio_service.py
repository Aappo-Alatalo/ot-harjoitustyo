from repositories.portfolio_repository import (
    portfolio_repository as default_portfolio_repo,
)

class PortfolioService:
    def __init__(self, portfolio_repo=default_portfolio_repo):
        self._portfolio_repo = portfolio_repo

    def add_funds(self, name, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if not name:
            raise ValueError("Name cannot be empty")

        print(f"Adding {amount} funds to portfolio {name}...")
        self._portfolio_repo.add_funds(name, amount)

    def subtract_funds(self, name, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if not name:
            raise ValueError("Name cannot be empty")

        print(f"Subtracting {amount} funds from portfolio {name}...")
        self._portfolio_repo.subtract_funds(name, amount)

    def get_funds(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        portfolio = self._portfolio_repo.get(name)
        if portfolio:
            return portfolio.funds
        else:
            raise ValueError(f"Portfolio with name {name} not found")
        
    def get_investments(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        investments = self._portfolio_repo.get_investments(name)
        if investments:
            return investments
        else:
            return print("No investments found for this portfolio.")
        
portfolio_service = PortfolioService()