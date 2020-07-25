'''
The function takes 2 strings and tell how many min(edits) (insert, delete and replace) need to be done to transform string 1 to string 2.
Example: "abc" -> "yabd" => 2 (insert 'y' and replace 'c' with 'd').

We build matrix to memorize every changes from None string line by line. 
If letters are equivalent, then we take value of change by diagonal left up from the matrix as replace edit. => current_line[j] = past_line[j - 1]
If no, then we take minimum of edits from elements before left and up left+up + 1 edit of extra letter => \
current_line[j] = 1 + min(current_line[j - 1], past_line[j], past_line[j - 1])

'''

# Version 1. O(nm) T / O(min(n,m)) S.
# We just save 2 lines of our memo matrix.
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    even = []
    for i in range(len(small) + 1):
        even.append(i)
    odd = [0] * (len(small) + 1)
	  current_line = odd
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            current_line = odd
            past_line = even
        else:
            current_line = even
            past_line = odd
        current_line[0] = i
        for j in range(1, len(small) + 1):
            if small[j - 1] == big[i - 1]:
                current_line[j] = past_line[j - 1]
            else:
                current_line[j] = 1 + min(current_line[j - 1], past_line[j], past_line[j - 1])

    return current_line[-1]
    
    
'''
# Version 2. O(nm) TS
# Simpler, handed with matrix.
def levenshteinDistance(str1, str2):
  matrix = []
	matrix.append(0)
	for i in range(len(str1)):
		matrix.append(i+1)
	matrix = [matrix]
  for j in range(len(str2)):
      matrix.append([j+1] * (len(str1) + 1))

	for i in range(len(str1)):
		for j in range(len(str2)):
			if str2[j] == str1[i]:
				matrix[j+1][i+1] = matrix[j][i]
			else:
				matrix[j+1][i+1] = min(matrix[j][i+1], matrix[j+1][i], matrix[j][i]) + 1
	
	return matrix[-1][-1]

    '''
