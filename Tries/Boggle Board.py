'''
Return words, which are in the board.
# board = [
#             ["t", "h", "i", "s", "i", "s", "a"],
#             ["s", "i", "m", "p", "l", "e", "x"],
#             ["b", "x", "x", "x", "x", "e", "b"],
#             ["x", "o", "g", "g", "l", "x", "o"],
#             ["x", "x", "x", "D", "T", "r", "a"],
#             ["R", "E", "P", "E", "A", "d", "x"],
#             ["x", "x", "x", "x", "x", "x", "x"],
#            ["N", "O", "T", "R", "E", "-", "P"],
#             ["x", "x", "D", "E", "T", "A", "E"],
#         ]
#
# words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]

board = [["a", "b"], ["c", "d"]]
words = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "abca"]

Output:
1) expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
2) expected = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb']
'''

# Create Trie and do DFS on each element in the array

def boggleBoard(board, words):
    trie = Trie(words)
    visited = [[False for letter in row] for row in board]

    found = {}
    for word in words:
        found[word] = False
    for col in range(len(board[0])):
        for row in range(len(board)):
            searchWord(board, col, row, visited, found, trie.trie)
    found_words = []
    for word in found:
        if found[word] is True:
            found_words.append(word)
    return found_words


def searchWord(board, col, row, visited, found, trie):
    if '*' in trie:
        found[trie['*']] = True

    if visited[row][col]:
        return
    letter = board[row][col]
    if letter in trie:
        visited[row][col] = True
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    continue
                if outOfBounders(board, r, c):
                    continue
                searchWord(board, c, r, visited, found, trie[letter])
        visited[row][col] = False


def outOfBounders(board, r, c):
    row = len(board)
    col = len(board[0])
    if r < 0 or r >= row:
        return True
    if c < 0 or c >= col:
        return True
    return False


class Trie:
    def __init__(self, words):
        self.trie = {}
        self.symbol = '*'
        for word in words:
            self.insertWord(word)

    def insertWord(self, word):
        local_head = self.trie
        for letter in word:
            if letter in local_head:
                local_head = local_head[letter]
            else:
                local_head[letter] = {}
                local_head = local_head[letter]
        local_head[self.symbol] = word
