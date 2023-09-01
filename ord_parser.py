from getpass import getpass

from parsers import ProfitLossParser


# TODO: Create a CLI
# TODO: Add colors
# TODO: Add progress bar
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
        activity_count = 0  # NOTE: TESTING
        flip_count = 0  # NOTE: TESTING

        for _id in parser.ordinal_data:
            print(_id)

            flip = parser.fetch_ordinal_data(ord_id=_id)

            if flip:
                print(flip)  # NOTE: TESTING
                flip_count += 1  # NOTE: TESTING
            activity_count += 1  # NOTE: TESTING
        print(f"Total activites parsed: {activity_count}")  # NOTE: TESTING
        print(f"Total full flips: {flip_count}")  # NOTE: TESTING
    else:
        print("No activity found")


if __name__ == "__main__":
    wallet = input("Enter wallet addr: ")
    api_key = getpass('Enter api token: ')

    main(
        wallet=wallet,
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {}
    )
