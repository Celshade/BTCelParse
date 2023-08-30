from getpass import getpass

from parsers import ProfitLossParser


# TODO: Create a CLI
# TODO: Add colors
# TODO: Add progress bar
def main(**kwargs) -> None:
    params = kwargs  # Should be valid query params from ME docs
    # GET wallet activity

    parser = ProfitLossParser(wallet=kwargs.get("wallet"))
    num_activites, activities = parser.get_activities(
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
