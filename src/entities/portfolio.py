class Portfolio:
    def __init__(
        self,
        portfolio_id,
        name,
        funds
    ):
        self.portfolio_id = portfolio_id
        self.name = name
        self.funds = funds

    def __repr__(self):
        return (
            f"Portfolio("
            f"id={self.portfolio_id}, "
            f"name={self.name}, "
            f"funds={self.funds})"
        )
