'''
Knuth Morris Pratt Algorithm aims to define if "string" contains "substring"
in O(n + m) time and o(m) space complexity, where
n - len(string)
m - len(substring)

1. Substring:
  1) Define patterns in the substring. Create array patterns to save indexes of 
  found patterns (p) before, else '-1'.
  2) Use 2 pointers j = 0 and i = 1. Move along the way to define such patterns,
  refer to patternSearch().
  3) When we come to the case where j != 0 and s[j] != st[i], then 
  use patterns to check if we saw a half of that pattern before to not return
  j index to the beginning of the subarray. If still s[p[i-1]+1] != st[i] no -> p[i] = '-1'.
2. Find substring in string:
  1) Use 2 pointers, where i is for main string, j is more substring.
  2) Same logic as creating patterns.
'''

def knuthMorrisPrattAlgorithm(string, substring):
    patterns = patternSearch(substring)
    i = 0
    j = 0
    while i < len(string):
        if string[i] == substring[j]:
            j += 1
            i += 1
        else:
            if j != 0:
                j = patterns[j - 1] + 1
                if substring[j] == string[i]:
                    i += 1
                    j += 1
                else:
                    j = 0
            else:
                i += 1
        if j == len(substring):
            return True
    return False


def patternSearch(string):
    patterns = [-1] * len(string)
    i = 1
    j = 0
    while i < len(string):
        if string[j] != string[i]:
            if j != 0:
                j = patterns[j - 1] + 1
        else:
            patterns[i] = j
            j += 1
        i += 1
    return patterns

