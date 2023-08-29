class ProfitLossParser():
    """
    TODO: Add docs.
    """

    def __init__(self, wallet: str) -> None:
        self.wallet = wallet

    # TODO: prefer generators over lists to save memory when reading in
    # TODO: Only looking for buy/sell per ordinal -> consolidate in dict?
    # TODO: Write to local file after parse?
    # TODO: Only configure for ME to start with (other marketplaces?)
