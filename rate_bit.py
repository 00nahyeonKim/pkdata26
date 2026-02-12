import requests as req

bit_url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
rate_url = "https://oapi.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=7nQyCm0nUHZxkTqTHh2IHZTV73RWl4y4&data=AP01"

res_bit = req.get(bit_url).json()
res_rate = req.get(rate_url).json()

bit_price = float(res_bit['price'])

raw_rate = res_rate[-1]['deal_bas_r']
rate = float(raw_rate.replace(",", ""))

total_won = int(bit_price * rate)

print(f"{total_won:,}원")