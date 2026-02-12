import requests as req

url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response_data = req.get(url).json()

price = float(response_data['price'])

won = str(int(price * 1450))
print(won[:1] + '억' + won[1:5] + '만' + won[5:] + '원')