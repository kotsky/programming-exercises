'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        
        if len(A) <= 1 or B == 1:
            return A

        res = []
        for i in range(B):
            res.append('')
            
        j = -1
        dir = 1
        
        for i in range(len(A)):
            
            j += dir
            res[j] += A[i]
            
            if j == B-1:
                dir = -1
            elif j == 0:
                dir = 1
            
        return ''.join(res)
            
            
            
