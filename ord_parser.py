import json
from pprint import pprint

import requests


ME_BASE_ADDR = "api-mainnet.magiceden.dev/v2/ord"
ME_ACTIVITY_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/activities"
ME_COLLECTION_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/collections/"


def get_activities(wallet=str, headers: dict[str, str] = {}):
    res = requests.get(
        ME_ACTIVITY_EP,
        params={"ownerAddress": wallet},
        headers=headers
    )

    if res.status_code == 200:
        return json.dumps(res.json())
    else:
        print("Error in request")
        return res.text


# NOTE: Testing
def get_collection(collection_symbol: str, headers: dict[str, str] = {}):
    res = requests.get(
        f"{ME_COLLECTION_EP}/{collection_symbol}",
        params={"symbol": "btck"},
        headers=headers
    )

    if res.status_code == 200:
        return json.dumps(res.json())
    else:
        print("Error in request")
        return res.text


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
    pprint(
        get_activities(
            wallet=kwargs.get("wallet"),
            headers=kwargs.get("headers", {})
        )
    )


if __name__ == "__main__":
    main(
        # symbol=input("Enter collection symbol: "),
        wallet=input("Enter wallet addr: "),
        headers={"Authorization": f"Bearer {input('Enter api token: ')}"}
    )
