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

    # Important counters
    activity_counter = 0  # Running total of parsed activities
    offset = 0  # pagination counter for API results
    confirmed_buys = 0
    confirmed_flips = 0
    confirmed_sales = 0
    profits = 0
    potential_profits = 0

    while "parsing":
        # Init parser and get wallet activity
        parser = ProfitLossParser(wallet=wallet)
        activities = parser._get_activities(
            headers=kwargs.get("headers"),
            offset=offset
        )
        offset += 1  # Increment offset pagination

        # Output total activity
        if activity_counter < 1:
            # Handle weird offset count bug from ME
            if parser.num_activities <= 40:
                count = parser.num_activities
            else:
                count = parser.num_activities - 1
            print(f"Buy/Sell activity count: {count}")

        if activities:
            parser._parse_activities(activities=activities)

            for _id in parser.ordinal_data:
                ord_data = parser.ordinal_data[_id]

                # Calculate flips
                flip = ord_data["flip"] if ord_data["flip"].flipped else None
                if flip:
                    print(flip)
                    confirmed_flips += 1
                    activity_counter += 2
                    confirmed_sales += 1
                    profits += flip.profit
                else:  # Calculate sales w/no purchase data
                    activity_counter += 1
                    if ord_data["flip"].purchased:
                        confirmed_buys += 1
                    elif ord_data["flip"].sold:
                        potential_profits += ord_data["flip"].sale_price
                        confirmed_sales += 1

        # print(f"**counter progress: {activity_counter}")  # NOTE: Testing
        if activity_counter >= parser.num_activities - 1:
            break

    print(f"Total confirmed flips: {confirmed_flips}")
    print(f"Total confirmed buys: {confirmed_buys}")
    print(f"Total confirmed sales: {confirmed_sales}")
    print(f"Total confirmed P/L: {clean_price(profits)}")
    print(f"Total unconfirmed P/L: {clean_price(potential_profits)}")
    print(
        f"Total potential P/L: {clean_price(profits + potential_profits)}"
    )
# else:
#     print("No activity found")


if __name__ == "__main__":
    wallet = getpass("Enter wallet addr: <censored for demo>")
    api_key = getpass('Enter api token: ')
    print("Using API key! 💪\n") if api_key else print()

    main(
        wallet=wallet,
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {}
    )
