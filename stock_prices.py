# O(n^2) complexity 
def get_max_profit1(stock_prices_yesterday):

    i  = len (stock_prices_yesterday)
    j = 1
    max_profit = 0

    for price in stock_prices_yesterday:

        for n in range(j,i):
            profit = price - n
            if profit > max_profit:
                max_profit = profit
        j = j+1
    
    return profit 

# O(n) complexity 
def get_max_profit2(stock_prices_yesterday):

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    min_price = stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):
        if index == 0: continue

        current_profit = current_price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, current_price)
    
    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit2(stock_prices_yesterday)