'''
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more
details about roman numerals at Roman Numeric System



Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
'''


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        
        res = 0
        i = 0
        l_t = 0
        l_d = 0
        
        while i < len(A):
            
            temp = ''
            
            while i < len(A):
                temp += A[i]
                t, d, flag = LUT(temp)
                if flag == True:
                    l_t = t
                    l_d = d
                    
                    if i == (len(A) - 1):
                        res += (l_d + 1)*pow(10,l_t)
                        return res
                else:
                    res += (l_d + 1)*pow(10,l_t)
                    flag = False
                    break
                i += 1

        
def LUT(num):
    
    lut = [['I','II','III','IV','V','VI','VII','VIII','IX'],
    ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
    ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
    ['M','MM','MMM', '', '','','','','']]
    
    flag = False
    
    for t in range(4):
        for d in range(9):
            if num == lut[t][d]:
                flag = True
                return t, d, flag
    
    return 0, 0, flag
