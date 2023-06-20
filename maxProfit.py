# Каждый день производится по одной единице продукции. 
# Каждый день устанавливается цена на товар
# Какую максимальную выгоду можно извлечь
# [1,3,2,5,1,3] -> 26

def maxProfit(prices: list) -> int:
    max = prices[-1]
    counter = 1
    result = 0
    for price in prices[-2::-1]:
        if price <= max:
            counter += 1
        else:
            result += max * counter
            counter = 1
            max = price
    result += max * counter
    return result

print(maxProfit([1,3,2,5,1,3]))
print(maxProfit([1,3,1,2]))