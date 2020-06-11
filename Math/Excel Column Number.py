'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''


	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
        ascii_offset = 64
        total_number = 0
        
        for i in range(len(A)):
            number = ord(A[-1-i]) - ascii_offset
            total_number += number * (26**i)
            
        return total_number


    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ost = A
        base = 26
        ascii_offset = 64
        res = []
    
        while ost > 0:
    
            if ost % base == 0:
                letter = base + ascii_offset
                adjust = 1
            else:
                letter = ost % base + ascii_offset
                adjust = 0
    
            if ost <= base:
                res.append(chr(letter))
                break
    
            res.append(chr(letter))
    
            ost = int(ost / base) - adjust
    
        res = res[::-1]
    
        res = "".join(res)
    
        return res
        
        
