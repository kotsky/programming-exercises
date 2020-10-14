# Failed: at one test case {"strings": ["foo", "baz", "foobar", "foobarbaz"]},
# where i didn't implement recursion check of a part of the word as its continue

'''
https://www.algoexpert.io/assessments/Special%20Strings
'''

def specialStrings(strings):
	if len(strings) < 2:
		return []
    dic = Trie(strings)
    return getListOfSpecial(strings, dic)


def getListOfSpecial(strings, dic):
    list_of_special = []
    for string in strings:
        if isSpecial(string, dic.root, 0, 0, dic):
            list_of_special.append(string)
    return list_of_special


def isSpecial(word, node, idx, count, trie):
	letter = word[idx]
	if letter not in node:
		return False
	
	atEndOfWord = idx == len(word) - 1
	if atEndOfWord:
		return '*' in node[word[idx]] and count + 1 >= 2
	
	if '*' in node[letter]:
		restIsSpecial = isSpecial(word, trie.root, idx + 1, count + 1, trie)
		if restIsSpecial:
			return True
	
	return isSpecial(word, node[letter], idx + 1, count, trie)
	
			
class Trie:
	def __init__(self, words):
		self.root = {}
		for wordIdx in range(len(words)):
			word = words[wordIdx]
			self.insertWord(word, wordIdx)
	
	def insertWord(self, word, wordIdx):
		node = self.root
		for i in range(len(word)):
			letter = word[i]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node['*'] = word
			
