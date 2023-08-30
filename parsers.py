import requests

from utils import HEADER, ACTIVITY, ME_ACTIVITY_EP


class ProfitLossParser():
    """
    TODO: Add docs.
    """

    def __init__(self, wallet: str) -> None:
        self.wallet = wallet
        self.ordinal_data: dict = {}

    def get_activities(
            self,
            headers: HEADER = {}
    ) -> tuple[int, list[ACTIVITY]]:
        """
        Return the [number of and] broadcasted activities for the given wallet.

        Only returns `buying_broadcasted` activity - ignoring arbitrary listings
        and transfers.

        Args:
            headers: Any special headers to include in the requests (default={}).
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
                return data.get("total"), data.get("activities")
            else:
                print("Error in request")
                return res.text
        except Exception as e:
            raise e

    # TODO: Write to local file after parse?
    # TODO: Only configure for ME to start with (other marketplaces?)
