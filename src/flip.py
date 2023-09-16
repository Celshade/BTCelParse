from utils import clean_price


class Flip():
    """
    TODO: Add docs.
    """

    def __init__(
            self,
            _id: str,
            purchased: str | None = None,
            purchase_price: float | None = None,
            sold: str | None = None,
            sale_price: float | None = None
    ) -> None:
        self._id = _id
        self.purchased = purchased
        self.purchase_price = purchase_price
        self.sold = sold
        self.sale_price = sale_price

    # TODO: Implement
    # def __repr__(self) -> str:
    #     raise NotImplementedError

    def __str__(self) -> str:
        return '\n'.join(
            (
                f"Ordinal ID: {self._id}",
                f"Purchased: {self.purchased} for {self.purchase_price}",
                f"Sold: {self.sold} for {self.sale_price}",
                f"P/L: {self.profit}\n"
            )
        )

    @property
    def flipped(self) -> bool:
        return True if self.purchased and self.sold else False

    @property
    def profit(self) -> float | None:
        """
        Return the profit from the Flip().
        """
        return clean_price(
            price=self.sale_price - self.purchase_price
        ) if self.flipped else None
