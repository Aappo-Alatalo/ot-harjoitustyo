class Investment:
    def __init__(
        self,
        investment_id,
        investment_type,
        name,
        amount,
        purchase_price
    ):
        self.investment_id = investment_id
        self.type = investment_type
        self.name = name
        self.amount = amount
        self.purchase_price = purchase_price

    def __repr__(self):
        return (
            f"Investment("
            f"id={self.investment_id}, "
            f"type={self.type}, "
            f"name={self.name}, "
            f"amount={self.amount}, "
            f"purchase_price={self.purchase_price})"
        )
