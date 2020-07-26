'''
You are given an array of uniqe integers as = [1, 2, 3]
Find and return all possible power set of this array.
Ouput = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
'''

# Start from [] solution and go to the higher [], [1] and so on.
# Or dublicate power sets from the previous solution and
# insert (append) new value from the given array.

def powerset(array):
    power_set = [[]]
    for num in array:
      for i in range(len(power_set)):
        current_sub = power_set[i]
        power_set.append(current_sub + [num])
    return power_set
	
