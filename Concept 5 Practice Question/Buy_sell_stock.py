## Best time to buy and sell of a stock in a week
## we have an array Price = [7, 1, 5, 3, 6, 4]
## need to calculate 2 index where profit will be max


def Max_Profit(Price):
    l, r = 0, 1
    max_p = 0
    while r < len(Price):   ##------------>> 0(n)
        if Price[l] < Price[r]:
            profit = Price[r] - Price[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p



## we also apply another approach with 0(n)
def findMaxProfit(price):
    minP = float('inf')
    maxP = 0
    for i in range(len(price)):
        if price[i] <minP:
            minP = price[i]
        elif (price[i] - minP) > maxP:
            maxP = price[i] - minP
    return maxP








## driver call
price = [7, 1, 5, 3, 6, 4]
result = Max_Profit(price)
print(result)

result1 = findMaxProfit(price)
print(result1)
