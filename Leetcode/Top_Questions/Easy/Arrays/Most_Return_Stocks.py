'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

'''

def maxProfit(prices: list[int]) -> int:

    if not prices:
        return 0

    max_profit = 0

    for i in range(0, len(prices) - 1):
        if prices[i] < prices[i+1]:
            max_profit += prices[i+1] - prices[i]

    return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices)) # Exprected: 7