''' Check, if 2nd string is rotated based on 1st string

  string1 = 'waterbottle'
  string2 = 'erbottlewat'
  print(stringRotation(string1, string2))  # => True
  
The idea:
  1. Check if string2 contains preffix of string1.
  2. For each such prefix, check other letters in
  the same order as origin.
'''

# O(s1 * (s1 + s2)) Time / O(s1) Space

def stringRotation(string1, string2):
    def _isSubstring(string1, string2):
        # Can be optimized by using Knus-Morris-Pratt Algo
        flag = string2.find(string1)
        return True if flag >= 0 else False

    def _trueRotation(start_idx, string1, string2):
        for idx in range(start_idx, len(string1)):
            if string1[idx] != string2[idx-start_idx]:
                return False
        return True

    for idx in range(len(string1)-1, -1, -1):
        if _isSubstring(string1[:idx+1], string2):
            if _trueRotation(idx+1, string1, string2):
                return True
    return False
