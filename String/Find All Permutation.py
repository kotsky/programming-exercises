'''
The idea is to:
1) Count unique letters in small string
2) with 2 pointers and counter of passed unique letters in a big string, 
traverse big string and checking how many and which letters we already passed 
and does that particular part of len(smallString) was covered in bigString?

Example:
    smallString = "abbc"
    bigString = "fabcbsfbabc"
    output = [1, 7], 2
    print(findAllPermutation(smallString, bigString))
'''

def findAllPermutation(small_string, big_string):
    tableOfUniqueLetter = buildTableOfUniqueLetter(small_string)
    start_points = getStartIdxOfEachPermutation(big_string, tableOfUniqueLetter, len(small_string))
    return start_points


def getStartIdxOfEachPermutation(bigString, tableOfLetters, lengthOfSmallString):
    start_idx = []
    tableOfCurrentLetters = {}
    countOfUniqueLetter = 0
    referenceOfUniqueLetters = tableOfLetters["ref"]

    for idx in range(lengthOfSmallString):
        letter = bigString[idx]
        if letter not in tableOfLetters:
            continue
        if letter not in tableOfCurrentLetters:
            tableOfCurrentLetters[letter] = 0
        tableOfCurrentLetters[letter] += 1

        if tableOfCurrentLetters[letter] == tableOfLetters[letter]:
            countOfUniqueLetter += 1

    if countOfUniqueLetter == referenceOfUniqueLetters:
        start_idx.append(0)

    for idx in range(lengthOfSmallString, len(bigString)):
        prev_letter = bigString[idx - lengthOfSmallString]
        letter = bigString[idx]

        if prev_letter in tableOfLetters:
            if tableOfCurrentLetters[prev_letter] == tableOfLetters[prev_letter]:
                countOfUniqueLetter -= 1
            tableOfCurrentLetters[prev_letter] -= 1

        if letter not in tableOfLetters:
            continue

        if letter not in tableOfCurrentLetters:
            tableOfCurrentLetters[letter] = 0
        tableOfCurrentLetters[letter] += 1

        if tableOfCurrentLetters[letter] == tableOfLetters[letter]:
            countOfUniqueLetter += 1

        if countOfUniqueLetter == referenceOfUniqueLetters:
            start_idx.append(idx - lengthOfSmallString + 1)

    return start_idx



def buildTableOfUniqueLetter(string):
    table = {}
    referenceOfUniqueLetters = 0
    for letter in string:
        if letter not in table:
            table[letter] = 0
            referenceOfUniqueLetters += 1
        table[letter] += 1
    table["ref"] = referenceOfUniqueLetters
    return table
