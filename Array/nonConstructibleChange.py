'''
What is the minimum number that cannot be combined by given numbers in array?
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
'''

def nonConstructibleChange(coins):
	if not coins:
		return 1
    coins.sort()
	idx = 0
	current_change = 1
	while idx < len(coins) and current_change >= coins[idx]:
		current_change += coins[idx]
		idx += 1
	return current_change
