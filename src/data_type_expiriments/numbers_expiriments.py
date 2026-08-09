index = 10
print(index)

price = 10.99
print(price)

priceFromText = float("10.98")
print(priceFromText + 4.02)

index_of_page = "2"
print(int(index_of_page) + 1)

actual_prices: list[str] = ["10.99", "99.43", "12.02"]
print(actual_prices)
print(max(actual_prices))
print(min(actual_prices))

def is_first_price_the_highest(t_prices: list[str]):
    return t_prices[0] == max(t_prices)

print(is_first_price_the_highest(actual_prices))
actual_prices.sort(reverse=True)
print(actual_prices)
print(is_first_price_the_highest(actual_prices))
