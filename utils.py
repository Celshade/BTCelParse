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

    Args:
        sats: The amount of sats to calculate.
    """
    return sats / SATS_IN_BTC
