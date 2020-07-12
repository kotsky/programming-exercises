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

def longestPalindromicSubstring(string):
	
	if len(string) <= 0:
		return None
	
    palindrom_index = [0, 0]
	
	for i in range(len(string)-1):
		
		left, right = palindromHelper(string, i, i)
		if (right - left) > (palindrom_index[1] - palindrom_index[0]):
			palindrom_index = [left, right]
			
		left, right = palindromHelper(string, i, i+1)
		if (right - left) > (palindrom_index[1] - palindrom_index[0]):
			palindrom_index = [left, right]
		
	return string[palindrom_index[0]:palindrom_index[1]+1]
		
def palindromHelper(string, left, right):
	while left >= 0 and right < len(string):
		if string[left] != string[right]:
			break		
		left -= 1
		right += 1
		
	return [left+1, right-1]
			
		
			
	
