'''
Define the longest chain from the given strings in descending order, where
each next string is made by removing one letter from the string before this chain.

strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"] 
print(longestStringChain(strings)) => ['abcdef', 'abcde', 'abde', 'ade', 'ae']

1. Convert to hash table for instant search.
2. Apply several additional key properties for easu navigation.
3. Define possible ways for each string to get another strings from the inout list.
4. Define which way is the longest by going recursively and tracking length and path.
5. Build the output array from the head => next_chain.
'''

# O(n*s^2) T / O(n*s) S, where
# n - len(strings)
# s - len of the longest string in strings

def longestStringChain(strings):
    stringsTable = stringsToTable(strings)
    linkChains(strings, stringsTable)
    chain_head = None
    max_length = 0
    for string in strings:
        length_val = diveIntoString(string, strings, stringsTable, 0)
        if length_val > max_length:
            max_length = length_val
            chain_head = string

    if chain_head is None:
        return []

    return buildChain(chain_head, strings, stringsTable)


def buildChain(head, strings, stringsTable):
    chain = [head]
    node = head
    while next_chain_idx in stringsTable[node]:
        node = strings[stringsTable[node][next_chain_idx]]
        chain.append(node)
    return chain


def diveIntoString(string, strings, stringsTable, length_val):
    if length in stringsTable[string]:
        return stringsTable[string][length]
    else:
        stringsTable[string][length] = length_val

    for chain_idx in stringsTable[string][chains_idx]:
        next_string = strings[chain_idx]
        length_val = 0
        length_val += diveIntoString(next_string, strings, stringsTable, length_val)
        length_val += 1
        if length_val > stringsTable[string][length]:
            stringsTable[string][length] = length_val
            stringsTable[string][next_chain_idx] = chain_idx

    return length_val


def linkChains(strings, stringsTable):
    for string in strings:
        for i in range(len(string)):
            new_string = remoweLetter(i, string)
            if new_string in stringsTable:
                new_string_idx = stringsTable[new_string][idx]
                stringsTable[string][chains_idx].append(new_string_idx)


def remoweLetter(i, word):
    return word[0:i] + word[i + 1:]


def stringsToTable(strings):
    table = {}
    for i in range(len(strings)):
        if strings[i] not in table:
            table[strings[i]] = {idx: i, chains_idx: []}
    return table


idx = 'idx'
length = 'length'
chains_idx = 'chains_idx'
next_chain_idx = 'next_chain_idx'

