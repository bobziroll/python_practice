"""
Challenge:

I have an array stock_prices_yesterday where:

The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
The values are the price of Apple stock at that time, in dollars.
For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500

Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple
stock yesterday. For this problem, we won't allow "shorting"; you must buy before you sell.
"""


def best_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    for current_price in stock_prices_yesterday:
        min_price = min(min_price, current_price)
        max_profit = max(max_profit, current_price - min_price)
    return max_profit

# I copied this straight from Interview Cake. I couldn't figure it out the first time through. I was mixed up,
# thinking I was needing to "buy high and sell low" which obviously doesn't make sense. :P