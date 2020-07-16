'''
You have denominations. How many combination of them is possible to do to achieve given sum 'n'?
'''

def numberOfWaysToMakeChange(n, denoms):
    if n == 0:
		return 1
	
	ways = [0]*(n+1)
	ways[0] = 1
	
	for denom in denoms:
		index = denom
		while index <= n:
			ways[index] += ways[index - denom]
			index += 1
	return ways[-1]
