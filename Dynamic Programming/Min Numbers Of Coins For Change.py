'''
You have target amount of money $6. You have denominations [1, 2, 4]. 
How much coins you need to reach target amount of money, using only notes you have? What is the minimum one?
Answer = 2+4 => 1note+1note = 2 notes.
'''

def minNumberOfCoinsForChange(n, denoms):
    if n == 0:
        return 0
    memo = [float("inf")] * (n + 1)
    memo[0] = 0

    for den in denoms:
        for i in range(1, len(memo)):
            if i >= den:
                memo[i] = min(memo[i], memo[i - den] + 1)

    return -1 if memo[-1] == float("inf") else memo[-1]
