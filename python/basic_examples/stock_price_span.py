# https://leetcode.com/problems/online-stock-span/description/?envType=study-plan-v2&envId=leetcode-75
# https://www.youtube.com/watch?v=slYh0ZNEqSw

class StockSpanner:

    def __init__(self):
        self.stack = [] # a pair: [price, span] where span is the number of elements smaller than the price

    def next(self, price: int) -> int:
        span = 1

        while len(self.stack) > 0 and price >= self.stack[-1][0]: # get the price of the latest stock
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])

        return self.stack[-1][1]



if __name__ == "__main__":
    stockSpanner = StockSpanner()
    stockSpanner.next(100); # return 1
    stockSpanner.next(80); # return 1
    stockSpanner.next(60); # return 1
    stockSpanner.next(70); # return 2
    stockSpanner.next(60); # return 1
    stockSpanner.next(75); # return 4, because the last 4 prices(including today 's price of 75) were less than or equal to today's price.
    stockSpanner.next(85); # return 6