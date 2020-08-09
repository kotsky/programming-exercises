'''
To defind if given words are in the given big string.
Input = "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
                          Output = [True, False, True, True, False, True, False],
'''


# O(ns + bs) T / O(ns) S
# where n - number of substrings in smallStrings
# s - largest len element in smallStrings
# b - len of bigString

def multiStringSearch(bigString, smallStrings):
  isInString = [False] * len(smallStrings)
	tiers = Tiers(smallStrings)
	for i in range(len(bigString)):
		searchHelper(bigString, tiers, i, isInString)
	return isInString


def searchHelper(bigString, tiers, i, isInString):
    node = tiers.root
    while i < len(bigString):
        if bigString[i] not in node:
            break
        else:
            node = node[bigString[i]]
            i += 1
        if '*' in node:
            isInString[node['*']] = True
            if len(node) == 1:
                break

class Tiers:
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
			if i == len(word)-1:
				node['*'] = wordIdx
		
				
'''
# Version 2.
# O(bn+sn) T average and O(bns) T worst / O(n) S

def multiStringSearch(bigString, smallStrings):
    isInString = []
	for word in smallStrings:	
		#isInString.append(word in bigString)
		isInString.append(bigString.find(word) >= 0)	
		
	return isInString

'''
		
	
