import requests as req

url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response_data = req.get(url).json()

price = float(response_data['price'])

print(str(price * 1450) + '원')