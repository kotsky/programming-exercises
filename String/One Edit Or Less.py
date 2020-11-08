""" Exercise: One or Zero edit.

You have 2 strings: string1 and string2. Check, if you can
do one time or zero insert/delete/replace to have same 
anagramma of string2 and string 1.

Examples:
  pale - bake -> False
  pale - bale -> True
  
The idea behind is the following: 
  1. Use hash tables. Count unique letters both strings.
  2. Subtract one table values from other one.
  3. Count have many edits you need.
  4. Check with your conditions: 1 edit or less.

"""

# O(s1 + s2) Time / Space complexity.
# where s1 - len(string1) and 
# s2 - len(string2)

def isOneEditOrLess(string1, string2):
    t1 = getTable(string1) 
    t2 = getTable(string2)
    
    t2 = deltaMergeTables(t1, t2)

    count_neg = 0
    count_pos = 0
    for unique_letter in t2:
        if t2[unique_letter] == 0:
            pass
        else:
            if t2[unique_letter] < 0:
                count_neg += t2[unique_letter]
            else:
                count_pos += t2[unique_letter]
                
    if count_pos <= 1 and count_neg >= -1:
        is_one_edit = True
    else:
        is_one_edit = False
    return is_one_edit

# Merge negatively 2 t1 and t2 hast tables
# into one t2. Simply t2 = t2 - t1

def deltaMergeTables(t1, t2):
    for letter_from_1 in t1:
        if letter_from_1 not in t2:
            t2[letter_from_1] = 0
        t2[letter_from_1] -= 1
    return t2


# Count all letter and write them down
# into hash table

def getTable(s):
    table = {}
    for letter in s:
        if letter not in table:
            table[letter] = 0
        table[letter] += 1
    return table

print(isOneEditOrLess('pale', 'bake'))
