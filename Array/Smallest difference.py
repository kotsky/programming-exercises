'''
To find out pair from 2 arrays with the smallest difference.
Return it as [arrayOne[], arrayTwo[]].
'''


def smallestDifference(arrayOne, arrayTwo):
    
	arrayOne.sort()
	arrayTwo.sort()
	
	mini = float("inf")
	p1 = 0
	p2 = 0
	
	while p1 < len(arrayOne) and p2 < len(arrayTwo):

		if mini > abs(arrayOne[p1] - arrayTwo[p2]):
			mini = abs(arrayOne[p1] - arrayTwo[p2])
			answer = [arrayOne[p1], arrayTwo[p2]]
		
		if mini == 0:
			return [arrayOne[p1], arrayTwo[p2]]
		
		if arrayOne[p1] < arrayTwo[p2]:
			p1 += 1
		else:
			p2 += 1
			
	return answer
	
