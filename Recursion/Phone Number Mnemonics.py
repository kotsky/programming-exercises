def phoneNumberMnemonics(phone_number):
	
	database = {
		'0': ['0'],
		'1': ['1'],
		'2': ['a', 'b', 'c'],
		'3': ['d', 'e', 'f'],
		'4': ['g', 'h', 'i'],
		'5': ['j', 'k', 'l'],
		'6': ['m', 'n', 'o'],
		'7': ['p', 'q', 'r', 's'],
		'8': ['t', 'u', 'v'],
		'9': ['w', 'x', 'y', 'z']
	} 
	
    current_mnemonics = [''] * len(phone_number)

    return phone_number_mnemonic_helper(phone_number, current_mnemonics,
                                        [], database, 0)


def phone_number_mnemonic_helper(phone_number, current_mnemonics,
                                 list_of_mnemonics, database, number_idx):
    if number_idx == len(phone_number):
        list_of_mnemonics.append(''.join(current_mnemonics.copy()))
        return list_of_mnemonics

    number = phone_number[number_idx]
    for letter in database[number]:
        current_mnemonics[number_idx] = letter
        phone_number_mnemonic_helper(phone_number, current_mnemonics,
                                     list_of_mnemonics, database, number_idx + 1)

    return list_of_mnemonics
