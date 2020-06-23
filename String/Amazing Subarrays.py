'''
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        mod = 10003
        count = 0

        for i in range(len(A)):
            if vowel(A[i]):
                count += len(A) - i
                count = count % mod
        return count
                
                
def vowel(letter):
    vow = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vow:
        return True
    else:
        return False
    
   
