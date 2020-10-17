'''
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile.  On each player's turn, 
that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only 
if Alice wins the game otherwise return False, assuming both players play optimally.

We can iterate all possible movements, and check if we can move to a False state. 
If we can, then we found a must-win strategy, otherwise, 
we must lose since the opponent has a must-win strategy in this case.
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        cache = {}
        def dfs(remain, cache):
            if remain == 0:
                return False
            
            if remain in cache:
                return not cache[remain]
            
            sqr = int(remain**0.5)
            for i in range(1, sqr+1):
                cache[remain] = dfs(remain - i*i, cache)
                if not cache[remain]:
                    return True
                
            return False
        return dfs(n, cache)
