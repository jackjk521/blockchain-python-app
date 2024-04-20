import requests
from prices import btc_price, eth_price, xrp_price, sol_price

# response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")

btc = btc_price.json()["data"]
eth = eth_price.json()["data"]
xrp = xrp_price.json()["data"]
sol = sol_price.json()["data"]


# print(btc["amount"])

def main():
    menuInput()

def menu():
    print('''
    Welcome! Please make a choice from the following menu

    1. Bitcoin
    2. Ethereum
    3. Ripple
    4. Solana
    5. Exit
    ''')

def menuInput():
    while True:
        menu()
        try:
            userChoice = int(input('Please make a selection: '))
        except ValueError:
            print('Please enter a whole number between 1 and 5')
            continue

        if userChoice < 1 or userChoice > 4:
            print('Please enter a number between 1 and 5')
        elif userChoice == 1:
            print('Current Bitcoin Price: $' + btc["amount"] )
        elif userChoice == 2:
            print('Current Ethereum Price: $' +  eth["amount"] )
        elif userChoice == 3:
               print('Current Ripple Price: $' +  xrp["amount"] )
        elif userChoice == 4:
            print('Current Solana Price: $' +  sol["amount"] )
        elif userChoice == 5:
            print('Thank you! Exiting the program.')
            break

# Calls main to start the program
main()

# response = requests.get("https://coinmarketcap.com/currencies/")
# response = requests.get("https://coinmarketcap.com/currencies/bitcoin/"
# print(response.text)