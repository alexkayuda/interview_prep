# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices: list[int]) -> int:

    if not prices:
        return 0

    min_price = float('inf') # 99999999999
    max_profit = 0

    for price in prices:

        # if "current" price is less then known min_price -> it becomes lowest price
        if price < min_price:
            min_price = price

        # if the difference between the "current" price and a min_price is bigger 
        # then known lowest price -> it becomes biggest profit
        if price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit



if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]    # Buy at 1, sell at 6, profit = 5
    prices2 = [7, 6, 4, 3, 1]       # 0 because we can't sell higher

    print(maxProfit(prices1))
    print(maxProfit(prices2))