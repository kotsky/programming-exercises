'''


string = "Tim is great    " => "    great is Tim"


'''

def reverseWordsInString(string):
    if not string:
        return ""

    reversed_string_array = []
    start_p = len(string)-1
    end_p = start_p

    SPACE = " "

    while end_p >= 0:
        if string[start_p] == SPACE:
            while end_p >= 0 and string[end_p] == SPACE:
                end_p -= 1
        else:
            while end_p >= 0 and string[end_p] != SPACE:
                end_p -= 1
        reversed_string_array.append(string[end_p + 1:start_p + 1])
        start_p = end_p

    return "".join(reversed_string_array)
