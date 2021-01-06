import yfinance as yf


data = yf.download("AAPL", start="2020-02-18", end="2020-03-24")
# data = yf.download("AAPL", start="2020-3-19", end="2020-4-20")
print(data)

number1 = 80.65
number2 = 57.02

print((number2 - number1) / number2 * 100)
