import json
from pprint import pprint
from getpass import getpass
from types import GeneratorType

import requests


# TYPES
HEADER = dict[str, str]
ACTIVITY = dict[str, str | int]

# PATHS
ME_BASE_ADDR = "api-mainnet.magiceden.dev/v2/ord"
ME_ACTIVITY_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/activities"
# ME_COLLECTION_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/collections/"


def get_activities(
        wallet=str,
        headers: HEADER = {}
) -> tuple[int, list[ACTIVITY]]:
    """
    Return the [number of and] broadcasted activities for the given wallet.

    Only returns `buying_broadcasted` activity - ignoring arbitrary listings
    and transfers.

    Args:
        wallet: The wallet activity to parse.
        headers: Any special headers to include in the requests (default={}).
    """
    try:
        res = requests.get(
            ME_ACTIVITY_EP,
            params={"ownerAddress": wallet, "kind": "buying_broadcasted"},
            headers=headers
        )

        if res.status_code == 200:
            # NOTE: >> {"total": int, "activities": list[ACTIVITY]}
            data = res.json()
            return data.get("total"), data.get("activities")
        else:
            print("Error in request")
            return res.text
    except Exception as e:
        raise e


# TODO: Create a CLI
# TODO: Add colors
# TODO: Add progress bar
def main(**kwargs) -> None:
    params = kwargs  # Should be valid query params from ME docs
    # NOTE: GET collection data
    # print(
    #     get_collection(
    #         collection_symbol=kwargs.get("symbol"),
    #         headers=kwargs.get("headers", {})
    #     )
    # )
    # NOTE: GET wallet activity

    num_activites, activities = get_activities(
        wallet=kwargs.get("wallet"),
        headers=kwargs.get("headers", {})
    )
    print(f"Buy/Sell activity count: {num_activites}")
    print(activities[0])


if __name__ == "__main__":
    main(
        # symbol=input("Enter collection symbol: "),
        wallet=input("Enter wallet addr: "),
        headers={"Authorization": f"Bearer {getpass('Enter api token: ')}"}
    )
