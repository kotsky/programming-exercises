'''
Defind min number of operations (insert, delete, replace)
to convert string1 into string2.

  >>> string1 = 'pala'
  >>> string2 = 'bala'

  >>> print(minNumberOfEdits(string1, string2)) # => 1
  
The idea behind: 
  1. Using DP methods. Build table of edit numbers for each letter.
  2. If letters are same, then we assume we can just take value
  by diagonal (means that we don't need do something with current
  letter).
  2. If letters are different, we try to understand, which operation
  we should perform: insert (take value up), delete (take value left)
  or replace (take value diagonal up-left). Add +1 as addition operation.
  3. Return last value of the table.
'''


# O(s1 + s2) Time / O(s1 * s2) Space

def minNumberOfEdits(string1, string2):
    table_of_changes = getPreBuiltTable(string1, string2)
    for row in range(1, len(string2)+1):
        for col in range(1, len(string1)+1):
            if string1[col-1] == string2[row-1]:
                table_of_changes[row][col] = table_of_changes[row-1][col-1]
            else:
                table_of_changes[row][col] = min(table_of_changes[row][col-1],
                                                 table_of_changes[row-1][col],
                                                 table_of_changes[row-1][col-1]) + 1
    return table_of_changes[-1][-1]


# Ex = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]

def getPreBuiltTable(string1, string2):
    table_of_changes = [[x + y for x in range(len(string1) + 1)] for y in range(len(string2) + 1)]
    return table_of_changes
