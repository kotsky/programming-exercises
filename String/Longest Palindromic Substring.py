'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        
        if len(A) < 1:
            return ''
        elif len(A) == 1:
            return A
            
        l = 0
        r = 0
        maxi = 0
        index_l = 0
        index_r = 0

        for i in range(len(A)):
            
            l, r = Solution.expandMid(A, i, i)
            
            if maxi < (r - l + 1):
                maxi = r - l + 1
                index_l = l
                index_r = r
            
            l, r = Solution.expandMid(A, i, i+1)
            
            if maxi < (r - l + 1):
                maxi = r - l + 1
                index_l = l
                index_r = r

        return A[index_l:index_r+1]
        
        

    def expandMid(s, left, right):
        
        st = 0
        e = 0
        flag = False
        
        while left >= 0 and right < len(s):
            
            if s[left] == s[right]:
                st = left
                e = right
                flag = True
            else:
                break
        
            left -= 1
            right += 1
        
        if flag == True:
            return st, e
        else:
            return 0, 0
            
            
            
            
            
                    
                    
