import json

import requests


ME_BASE_ADDR = "api-mainnet.magiceden.dev/v2/ord"
ME_ACTIVITY_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/activities"
ME_COLLECTION_EP = "https://api-mainnet.magiceden.dev/v2/ord/btc/collections/"


def get_activities(wallet=str, headers: dict[str, str] = {}):
    res = requests.get(ME_ACTIVITY_EP, params={"ownerAddress": wallet})

    if res.status_code == 200:
        return json.dumps(res.json())
    else:
        print("Error in request")
        return res.text


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


def main(**kwargs) -> None:
    params = kwargs  # Should be valid query params from ME docs
    # headers = []
    # print(get_activities(wallet=input("Enter wallet addr: ")))
    print(
        get_collection(
            collection_symbol=kwargs.get("symbol"),
            headers=kwargs.get("headers", {})
        )
    )


if __name__ == "__main__":
    main(
        symbol=input("Enter collection symbol: "),
        headers={"Authorization": f"Bearer {input('Enter api token: ')}"}
    )
