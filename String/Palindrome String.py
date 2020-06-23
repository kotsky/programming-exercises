'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        left = 0
        right = len(A)-1
        while left < right:

            while True:
                if (ord(A[left].lower()) <= 122 and ord(A[left].lower()) >= 97) or \
                (ord(A[left].lower()) <= 57 and ord(A[left].lower()) >= 48) :
                    break
                left += 1
                if left == right:
                    return "1"
            
            while True:
                if (ord(A[right].lower()) <= 122 and ord(A[right].lower()) >= 97) or \
                (ord(A[right].lower()) <= 57 and ord(A[right].lower()) >= 48) :
                    break
                right -= 1
                if left == right:
                    return "1"
                
            if A[left].lower() == A[right].lower():
                left += 1
                right -= 1
            else:
                return "0"
                
        return "1"
        
        
        
