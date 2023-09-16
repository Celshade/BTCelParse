# TYPES
HEADERS = dict[str, str]
ACTIVITY = dict[str, str | int]

# CONSTANTS
SATS_IN_BTC = 100000000

# PATHS
ME_BASE_ADDR = "api-mainnet.magiceden.dev/v2/ord"
ME_ACTIVITY_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/activities"


# FUNCS
def to_btc(sats: int) -> float:
    """
    Return the given sat value in bitcoin.

    Rounds to 4 decimals (i.e. 0.0001) aka the nearest US dollar.

    Args:
        sats: The amount of sats to calculate.
    """
    return round(sats / SATS_IN_BTC, ndigits=4)
