'''
Given string shift by key in order 'az' key = 1 -> 'ba'
'''

def caesarCipherEncryptor(string, key):
    answer = []
	for i in range(len(string)):
		answer.append(shiftLetter(string[i], key))
	return ''.join(answer)
	
def shiftLetter(letter, key):
	# a - 97
	# z - 122
	letter = ord(letter)
	shifted_letter = letter + key % 26
	if shifted_letter > 122:
		shifted_letter -= 26
	shifted_letter = chr(shifted_letter)	
	return shifted_letter
