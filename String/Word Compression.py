'''
compression()
You need to compress word = 'aaaabbbccdkkrr' into
'a3b3c2d1k2r2'.

runLengthEncoding() # bound up to 9 symbols
string = "AAAAAAAAAAAAABBCCCCDD"
expected = "9A4A2B4C2D"
'''

# O(N) Time / O(N) Space

def runLengthEncoding(string):
    compressed_array = [1, string[0]]
	for idx in range(1, len(string)):
		if compressed_array[-1] != string[idx] or compressed_array[-2] == 9:
			compressed_array.append(0)
			compressed_array.append(string[idx])
		compressed_array[-2] += 1
		
	for idx in range(0, len(compressed_array), 2):
		compressed_array[idx] = str(compressed_array[idx])
	
	return ''.join(compressed_array)


# O(N) Time / O(N) Space

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
