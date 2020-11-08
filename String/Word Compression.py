'''
You need to compress word = 'aaaabbbccdkkrr' into
'a3b3c2d1k2r2'.
'''

def compression(word):
    compressed_array = []
    letter_count = 0
    for idx in range(len(word)):
        if not compressed_array:
            compressed_array.append(word[idx])
            letter_count = 0
            continue
        if word[idx] == word[idx-1]:
            letter_count += 1
        else:
            compressed_array.append(str(letter_count))
            letter_count = 1
            compressed_array.append(word[idx])

    compressed_array.append(str(letter_count))
    return ''.join(compressed_array)

print(compression(word))
