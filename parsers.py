from typing import Generator

import requests

from utils import HEADERS, ACTIVITY, ME_ACTIVITY_EP


class ProfitLossParser():
    """
    TODO: Add docs.
    """

    def __init__(self, wallet: str) -> None:
        self.wallet = wallet
        self.num_activities: int = 0
        # TODO: annotdate timestamps
        self.ordinal_data: dict[str, str | int | any] = {}

    def _get_activities(
            self,
            headers: HEADERS
    ) -> Generator[ACTIVITY, None, None]:
        """
        Return the [number of and] broadcasted activities for the given wallet.

        Only returns `buying_broadcasted` activity - ignoring arbitrary listings
        and transfers.

        Args:
            headers: Headers to include in the requests (default={}).
        """
        try:
            res = requests.get(
                ME_ACTIVITY_EP,
                params={
                    "ownerAddress": self.wallet,
                    "kind": "buying_broadcasted"
                },
                headers=headers
            )

            if res.status_code == 200:
                # NOTE: >> {"total": int, "activities": list[ACTIVITY]}
                data = res.json()

                self.num_activities = data.get("total")
                return (activity for activity in data.get("activities"))
            else:
                print("Request error. Try again later.")
                print("*TIP* Provide an API key from ME to avoid this issue!")
                return res.text
        except Exception as e:
            raise e

    def _parse_activities(self, activities: list[ACTIVITY]) -> None:
        for act in activities:
            ord_id: str = act["tokenId"]

            if not self.ordinal_data.get(ord_id):
                # Verify buy or sale
                _type = "buy" if act["oldOwner"] == self.wallet else "sale"
                # Parse activity data
                self.ordinal_data[ord_id] = {
                    "collection": act["collection"]["name"],
                    "inscription": act["token"]["inscriptionNumber"],
                    "txn_type": _type,
                    "purchased": act["createdAt"] if _type == "buy" else None,
                    "purchase_price": int,  # TODO implement
                    "sold": act["createdAt"] if _type == "sale" else None,
                    "sale_price": int,  # TODO implement
                    "profit": int  # TODO implement
                }
            else:
                # TODO update
                raise NotImplementedError

    # TODO: public method to combo _get_activities() _parse_activities()

    def fetch_ordinal_data(ord_id: str) -> dict:
        """
        Return parsed buy/sell data for a single ordinal.

        Args:
            ord_id: The ID for the ordinal to fetch data on.
        """
        raise NotImplementedError

    def export(self) -> None:
        """
        Write ordindal buy/sell data to file.
        """
        raise NotImplementedError


# TODO: Handle maker/taker fees -> maker = ?% & taker = 2%
