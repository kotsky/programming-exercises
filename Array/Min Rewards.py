'''
Min Peak problem with its expansion.
Input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output: sum([4, 3, 2, 1, 2, 3, 4, 5, 1]) = 25
'''


# O(n) TS

def minRewards(scores):
	if len(scores) == 1:
		return 1
	
  rewards = [0]*len(scores)
	
	for i in range(len(scores)):
		if findPeak(i, scores):
			rewarding(i, scores, rewards)
	return sum(rewards)		
			
			
def rewarding(startIdx, scores, rewards):
	rewards[startIdx] = 1	# min rewards
	left = startIdx-1
	while left >= 0 and scores[left] > scores[left+1]:
		rewards[left] = max(rewards[left], rewards[left+1] + 1)
		left -= 1
	
	right = startIdx+1
	while right < len(scores) and scores[right-1] < scores[right]:
		rewards[right] = max(rewards[right], rewards[right-1] + 1)
		right += 1
	

def findPeak(i, scores):
	if i == 0:
		if scores[i] < scores[i+1]:
			return True
		return False
	elif i == len(scores)-1:
		if scores[i] < scores[i-1]:
			return True
		return False
	
	if scores[i] < scores[i+1] and scores[i] < scores[i-1]:
		return True
	else:
		return False
