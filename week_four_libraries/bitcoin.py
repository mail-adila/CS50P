#In a file called bitcoin.py, implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that
# they would like to buy. If that argument cannot be converted to a float, the program should
# exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index at
# rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the
# actual API key you obtained from your CoinCap account dashboard, which returns a JSON object,
# among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions,
# as with code like:
# import requests
#
# try:
#     ...
# except requests.RequestException:
#     ...
# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

import sys
import requests


def get_number_of_bitcoins():
    if len(sys.argv) == 2:
        try:
            coins = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")
    return coins

def get_current_price(bitcoins):
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="
                            "7169c3ffc41b647de9ddfdc6a026e5dcd1722a965f8fb0ec238b0348aeaf90a5")
        price_data = response.json()
        price = float(price_data["data"]["priceUsd"]) * bitcoins
        print(f"${price:,.4f}")
    except requests.RequestException:
        sys.exit("Couldn't connect to Bitcoin API")

def main():
    coins = get_number_of_bitcoins()
    get_current_price(coins)

if __name__ == "__main__":
    main()