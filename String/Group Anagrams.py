# words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
# to -> [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp']]

# Version 1
# O(w * n * log(n)) T / O(wn) S

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        alph_order = wordToAlphOrder(word)
        if alph_order not in anagrams:
            anagrams[alph_order] = [word]
        else:
            anagrams[alph_order].append(word)

    answer = []
    for word in anagrams.values():
        answer.append(word)
    return answer
	
	
# Function below takes input 'word' and
# return 'string' in alphabet order:
# 'cat' -> 'act'
# O(N * log(N)) T / O(N) S
# Alt: sortedWord = "".join(sorted(word))
def wordToAlphOrder(word):	
    string = []
    for letter in word:	
        string.append(ord(letter))
    string.sort()
    word = "".join(map(chr, string))
    return word
    
    
    
# Version 2

# O(w^2 * n) T / O(wn) S
def groupAnagrams(words):
    answer = []

    for i in range(len(words)):
        word = words[i]
        if word == 0:
            pass
        else:
            sub_answer = [word]
            for j in range(i + 1, len(words)):

                if words[j] == 0:
                    pass
                else:
                    if len(words[j]) != len(word):
                        pass
                    else:
                        sub_answer, flag = anaHelper(word, words[j], sub_answer)
                        if flag:
                            words[j] = 0
            answer.append(sub_answer)
    return answer


def anaHelper(word, string, sub_answer):
    toAdd = True
    for letter in word:
        if letter not in string:
            toAdd = False
            break
    if toAdd:
        sub_answer.append(string)

    return sub_answer, toAdd
