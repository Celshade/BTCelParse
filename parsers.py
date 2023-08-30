import requests

from utils import HEADERS, ACTIVITY, ME_ACTIVITY_EP


class ProfitLossParser():
    """
    TODO: Add docs.
    """

    def __init__(self, wallet: str) -> None:
        self.wallet = wallet
        self.num_activities: int = 0
        self.ordinal_data: dict = {}

    def _get_activities(
            self,
            headers: HEADERS
    ) -> tuple[int, list[ACTIVITY]]:
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
                return data.get("activities")
            else:
                print("Error in request")
                return res.text
        except Exception as e:
            raise e

    def _parse_activities(self, activities: list[ACTIVITY]) -> None:
        _id: str  # can be input on ordinals.com
        collection: str
        buy: bool
        sell: bool
        timestamp: any  # do we care?

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

    # TODO: Write to local file after parse?
    # TODO: Only configure for ME to start with (other marketplaces?)
