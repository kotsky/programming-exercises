"""
Word Squares: find words' setup to create 
a square, where row[i] = col[i].

["ball","area","lead","lady"]

b a l l
a r e a
l e a d
l a d y


Example:
    
    words = ["abat", "baba", "atan", "atal", "ball"]
    # words = ['aaaa', 'aaaa','aaaa','aaaa']
    print(word_square_builder(words))
    
Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

The idea:
1. Create a suffix search table.
2. Try to check if next word possible to use 
in our solution by checking it in suffix 
table.

"""

# Version 2:
# O(W * S^(W*S^2)) Time worst 
# O(S^S) Space worst 
# (when same letters like "aaa")
# and
# O(W * S^(W*S)) Time avg
# O(S^2) Space avg


def word_square_builder(words):
    suffix_table = build_suffix_table(words)
    return word_squares(suffix_table, words)


# O(W * S^2) Time / Space

def build_suffix_table(words):
    table = {}
    for word_idx in range(len(words)):
        word = words[word_idx]
        for letter_idx in range(len(word)):
            suffix = word[0:letter_idx+1]
            if suffix not in table:
                table[suffix] = [word_idx]
            else:
                table[suffix].append(word_idx)
    return table


def word_squares(suffix_table, words):
    squares = []
    for word in words:
        _, squares = explore_word(words, 1, suffix_table, [word], squares)
    return squares


""" 
Version 1

# O(S) Time / Space

# def get_suffix_from(square, idx):
#     suffix_array = []
#     for line in square:
#         suffix_array.append(line[idx])
#     return ''.join(suffix_array)

# O(S^(W*S^2))  Time worst (for "aaa", "aaa", "aaa")
# O(S^2) Space avg and O(S^S) worst (for "aaa", "aaa", "aaa")

# def explore_word(words, letter_idx, suffix_table, current_square, squares):
#
#     suffix_to_check = get_suffix_from(current_square, letter_idx)
#
#     if suffix_to_check in suffix_table:
#         words_idx_of_current_suffix = suffix_table[suffix_to_check]
#
#         for word_idx in words_idx_of_current_suffix:
#             current_square.append(words[word_idx])
#             if len(current_square) == len(words[0]):
#                 squares.append(current_square.copy())   # O(S^2)
#                 current_square.pop()
#                 continue
#             current_square, squares = explore_word(words, letter_idx+1,
#                                                    suffix_table, current_square,
#                                                    squares)
#     current_square.pop()
#     return current_square, squares
"""

# Version 2

def get_suffix_from(square, idx, letter):
    suffix_array = []
    for line in square:
        suffix_array.append(line[idx])
    suffix_array.append(letter)
    return ''.join(suffix_array)

# O(S^(W*S^2)) Time worst (for "aaa", "aaa", "aaa")
# but O(S^(W*S)) Time avg -> because we check suffix
# before appending possible word, what reduce time
# complexity in avg
# O(S^2) Space avg and O(S^S) worst (for "aaa", "aaa", "aaa")


def explore_word(words, letter_idx, suffix_table, current_square, squares):
    if len(current_square) == len(words[0]):
        squares.append(current_square.copy())
        current_square.pop()
        return current_square, squares

    suffix_to_check = get_suffix_from(current_square, letter_idx, '')

    if suffix_to_check in suffix_table:
        words_idx_of_current_suffix = suffix_table[suffix_to_check]

        for word_idx in words_idx_of_current_suffix:
            possible_word = words[word_idx]
            suffix_to_check = get_suffix_from(current_square, letter_idx, 
                                              possible_word[letter_idx])

            if suffix_to_check in suffix_table:
                current_square.append(words[word_idx])
                current_square, squares = explore_word(words, letter_idx+1,
                                                       suffix_table, current_square,
                                                       squares)
    current_square.pop()
    return current_square, squares
