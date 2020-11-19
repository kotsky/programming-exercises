'''
The idea here is that we just check with 2 pointers if letters from the start of string1 can be equvalent to the end letters of string2. 
When we reach point where letters are different, if check we the rest of string1 or string2 is palindrom.
'''

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkPalFromTwoStrings(a, b) or self.checkPalFromTwoStrings(b, a)
    
    def checkPalFromTwoStrings(self, str1, str2):
        p1 = 0
        p2 = len(str2)-1
        while p2-p1 > 0 and str1[p1] == str2[p2]:
            p2 -= 1
            p1 += 1
        
        return self.checkPalOneString(str1, p2, p1) or self.checkPalOneString(str2, p2, p1)
    
    def checkPalOneString(self, string, p2, p1):
        while p2-p1 > 0:
            if string[p1] != string[p2]:
                return False
            p2 -= 1
            p1 += 1
        return True
            
        
