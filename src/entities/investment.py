class Investment:
    def __init__(
        self,
        investment_id,
        investment_type,
        name,
        amount,
        purchase_price
    ):
        self._investment_id = investment_id
        self._type = investment_type
        self._name = name
        self._amount = amount
        self._purchase_price = purchase_price

    def __repr__(self):
        return (
            f"Investment("
            f"id={self._investment_id}, "
            f"type={self._type}, "
            f"name={self._name}, "
            f"amount={self._amount}, "
            f"purchase_price={self._purchase_price})"
        )
