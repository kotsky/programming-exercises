


class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        
        if A <= 1:
            return A
            
        n = A
        res = []
        while n > 1:
            if n / 2 >= 1 and n % 2 == 0:
                res.append(0)
            elif n / 2 >= 1 and n % 2 != 0:
                res.append(1)

            n = int(n / 2)

            if n == 1:
                res.append(1)
                n = res
                res = 0
                for i in range(len(n)):
                    res = res + n[i] * pow(10, i)
                
                return res

            
        
