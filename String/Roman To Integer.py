'''
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

For Example
    Input 1:
        A = "XIV"
    Output 1:
        14

    Input 2:
        A = "XX"
    Output 2:
        20
        
The idea: create LUT for pattern searching. If there is no respective
number in LUT, then we deal with new part of the number.
'''

# O(N) Time / O(1) Space

def romanToInt(A):

    res = 0
    i = 0
    l_t = 0
    l_d = 0

    while i < len(A):

        temp = ''

        while i < len(A):
            temp += A[i]    # max len(temp) is 5 symbols
            t, d, flag = LUT(temp)
            if flag == True:
                l_t = t
                l_d = d

                if i == (len(A) - 1):
                    res += (l_d + 1) * pow(10, l_t)
                    return res
            else:
                res += (l_d + 1) * pow(10, l_t)
                break
            i += 1

            
# LUT can be improved by using hash table
# 144 time (implementation below) vs 1 time hash

def LUT(num):
    lut = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
           ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['M', 'MM', 'MMM', '', '', '', '', '', '']]

    flag = False

    for t in range(4):
        for d in range(9):
            if num == lut[t][d]:
                flag = True
                return t, d, flag

    return 0, 0, flag
