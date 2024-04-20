import requests

btc_price = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
xrp_price = requests.get("https://api.coinbase.com/v2/prices/XRP-USD/spot")
sol_price = requests.get("https://api.coinbase.com/v2/prices/SOL-USD/spot")
eth_price = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
