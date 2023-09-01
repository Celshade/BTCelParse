from typing import Generator, Iterable

import requests

from flip import Flip
from utils import HEADERS, ACTIVITY, ME_ACTIVITY_EP, to_btc


class ProfitLossParser():
    """
    TODO: Add docs.
    """

    def __init__(self, wallet: str) -> None:
        self.wallet = wallet
        self.num_activities: int = 0
        self.ordinal_data: dict[str, str | int | any] = {}

    def _get_activities(
            self,
            headers: HEADERS
    ) -> Generator[ACTIVITY, None, None]:
        """
        Return the [number of and] broadcasted activities for the given wallet.

        Only returns `buying_broadcasted` activity - ignoring arbitrary listings
        and transfers.

        NOTE: The ME activity endpoint sorts by timestamp
        descending - this function will return sorted by ascending (oldest
        first).

        Args:
            headers: Headers to include in the requests (default={}).
        """
        try:
            res = requests.get(
                ME_ACTIVITY_EP,
                params={
                    "ownerAddress": self.wallet,
                    "kind": ["buying_broadcasted", "mint_broadcasted"]
                },
                headers=headers
            )

            if res.status_code == 200:
                # NOTE: >> {"total": int, "activities": list[ACTIVITY]}
                data = res.json()

                self.num_activities = data.get("total")
                return (
                    activity for activity in data.get("activities")[::-1]
                )
            else:
                print("Request error. Try again later.")
                print("*TIP* Provide an API key from ME to avoid this issue!")
                return res.text
        except Exception as e:
            raise e

    def _set_new_data(
            self,
            ord_id: str,
            activity: ACTIVITY,
            _type: str
    ) -> None:
        """
        Parse initial `ACTIVITY` data for the given ordinal.

        Args:
            ord_id: The ordinal ID.
            activity: The `ACTIVITY` to parse.
            _type: The txn type of `ACTIVITY` ('buy' | 'sale').
        """
        # Parse activityivity data
        self.ordinal_data[ord_id] = {
            # Ordinal data
            "collection": activity["collection"]["name"],
            "inscription": activity["token"]["inscriptionNumber"],
            "txn_type": _type,
            "flip": Flip(
                purchased=activity["createdAt"] if _type == "buy" else None,
                purchase_price=to_btc(
                    activity["listedPrice"]
                ) if _type == "buy" else None,
                sold=activity["createdAt"] if _type == "sale" else None,
                sale_price=to_btc(
                    activity["listedPrice"]
                ) if _type == "sale" else None
            )
        }

    def _update_data(
            self,
            flip_data: Flip,
            activity: ACTIVITY,
            _type: str | None
    ) -> None:
        """
        Update existing data for the given `ACTIVITY`.

        Args:
            flip_data: The `Flip()` object storing buy/sell data.
            activity: The `ACTIVITY` to parse.
            _type: The txn type of `ACTIVITY` ('buy' | 'sale').
        """
        # Update buy data
        if _type == "buy":
            flip_data.purchased = activity["createdAt"]
            flip_data.purchase_price = to_btc(activity["listedPrice"])
        elif _type == "sale":  # Update sale data
            flip_data.sold = activity["createdAt"]
            flip_data.sale_price = to_btc(activity["listedPrice"])
        else:
            print("Well this is awkward...")

    def _parse_activities(self, activities: Iterable[ACTIVITY]) -> None:
        for activity in activities:
            # Handle edge case where buyer == seller (dafuq)
            try:
                assert activity["oldOwner"] != activity["newOwner"]
            except AssertionError:
                print("Buyer == Seller; skipping.")
                continue

            # Establish ID and txn type
            ord_id: str = activity["tokenId"]
            # Establish txn type
            _type = "sale" if activity["oldOwner"] == self.wallet else "buy"

            if not self.ordinal_data.get(ord_id):
                # Parse initial data
                self._set_new_data(
                    ord_id=ord_id,
                    activity=activity,
                    _type=_type
                )
            else:  # Update existing data
                self._update_data(
                    flip_data=self.ordinal_data[ord_id]["flip"],
                    activity=activity,
                    _type=_type
                )

    # TODO: public method to combo _get_activities() _parse_activities()

    def fetch_ordinal_data(self, ord_id: str) -> dict:
        """
        Return parsed buy/sell data for a single ordinal.

        Args:
            ord_id: The ID for the ordinal to fetch data on.
        """
        ord_data = self.ordinal_data[ord_id]
        return ord_data["flip"] if ord_data["flip"].flipped else None
        # return ord_data["flip"]  # NOTE: TESTING

    def export(self) -> None:
        """
        Write ordindal buy/sell data to file.
        """
        raise NotImplementedError


# TODO: Handle maker/taker fees -> maker = ?% & taker = 2%
