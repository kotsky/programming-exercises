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

        
        
