from getpass import getpass

from parsers import ProfitLossParser
from utils import clean_price


# TODO: Create a CLI
# TODO: Add colors
# TODO: Add progress bar
# TODO: Improve output formatting
# TODO: Implement export()
# TODO: Implement json
def main(**kwargs) -> None:
    """
    Call the ProfitLossParser() to parse ordinal buys/sells.

    Providing an API key is optional; however, if one is not provided, the
    requests may fail to return results.
    """
    wallet = kwargs.get("wallet")

    # Validate wallet
    if not wallet:
        print("No wallet provided")

    # Init parser and get wallet activity
    parser = ProfitLossParser(wallet=wallet)
    activities = parser._get_activities(headers=kwargs.get("headers"))

    if activities:
        print(f"Buy/Sell activity count: {parser.num_activities}")
        # print(list(activities)[0])  # NOTE: TESTING
        parser._parse_activities(activities=activities)

        confirmed_flips = 0
        confirmed_sales = 0
        profits = 0
        potential_profits = 0

        for _id in parser.ordinal_data:
            # print(_id)  # NOTE: TESTING
            ord_data = parser.ordinal_data[_id]

            # Calculate full flips
            # flip = parser.fetch_flip(ord_data=ord_data)
            flip = ord_data["flip"] if ord_data["flip"].flipped else None
            if flip:
                print(flip)  # NOTE: TESTING
                confirmed_flips += 1
                confirmed_sales += 1
                profits += flip.profit
            else:  # Calculate sales w/no purchase data
                if ord_data["flip"].sold:
                    potential_profits += ord_data["flip"].sale_price
                    confirmed_sales += 1
        # NOTE: TESTING
        print(f"Total confirmed flips: {confirmed_flips}")
        print(f"Total confirmed sales: {confirmed_sales}")
        print(f"Total confirmed P/L: {clean_price(profits)}")
        print(f"Total unconfirmed P/L: {clean_price(potential_profits)}")
        print(
            f"Total potential P/L: {clean_price(profits + potential_profits)}"
        )
    else:
        print("No activity found")


if __name__ == "__main__":
    wallet = input("Enter wallet addr: ")
    api_key = getpass('Enter api token: ')
    print("Using API key! 💪\n") if api_key else print()

    main(
        wallet=wallet,
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {}
    )
