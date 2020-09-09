'''
Max profit from k transaction, where 1 transaction is buy/sell. You can hold only 1 stock at one time.
prices is the given array of prices per day (indexes).
'''

# Memo style with point of how much money we can gain if we
# sell that stock at that particular day (idx).
# When we sold it out, what was the max profit at k-1
# line at day before we sold out and to summarize it.
# Compare with the last day value of trading and choose
# the max.

def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    profit_prev = [0] * (len(prices))
    profit_current = [0] * (len(prices))

    for tr in range(1, k + 1):
        max_prof_pref_tr = float("-inf")
        profit_next = profit_prev
        profit_prev = profit_current
        profit_current = profit_next
        for day in range(1, len(prices)):
            max_prof_pref_tr = max(max_prof_pref_tr, profit_prev[day - 1] - prices[day - 1])
            profit_current[day] = max(profit_current[day - 1], max_prof_pref_tr + prices[day])
    return profit_current[-1]


print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 3))
