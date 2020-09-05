'''
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Are "one" and "two" interweaving strings?

print(interweavingStrings(one, two, three))
'''
# O(len(one) * len(two)) TS

def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
        return False
    memo = {}
    return checkInterweavingFromThePointer(one, two, three, 0, 0, memo)

def checkInterweavingFromThePointer(one, two, three, p1, p2, memo):
    if chr(p1) + '_' + chr(p2) in memo:
        return memo[chr(p1) + '_' + chr(p2)]

    p = p1 + p2
    if p == len(three):
        return True

    if p1 < len(one) and three[p] == one[p1]:
        cache = checkInterweavingFromThePointer(one, two, three, p1 + 1, p2, memo)
        memo[chr(p1) + '_' + chr(p2)] = cache
        if cache:
            return True

    if p2 < len(two) and three[p] == two[p2]:
        cache = checkInterweavingFromThePointer(one, two, three, p1, p2 + 1, memo)
        memo[chr(p1) + '_' + chr(p2)] = cache
        return cache

    memo[chr(p1) + '_' + chr(p2)] = False
    return False

'''
# Without memo: O(2^(o+t)) T / O(ot) S

def interweavingStrings(one, two, three):
    if len(one)+len(two) != len(three):
		return False
	return checkInterweavingFromThePointer(one, two, three, 0, 0)
	
	
def checkInterweavingFromThePointer(one, two, three, p1, p2):
	p = p1 + p2
	if p == len(three):
		return True
	
	if p1 < len(one) and three[p] == one[p1]:
	    if checkInterweavingFromThePointer(one, two, three, p1+1, p2):
			return True
	
	if p2 < len(two) and three[p] == two[p2]:
		if checkInterweavingFromThePointer(one, two, three, p1, p2+1):
			return True
		
	return False
'''
	
		
