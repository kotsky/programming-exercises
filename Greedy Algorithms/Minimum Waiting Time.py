"""

Define min waiting time for queries to be executed, if
in queries[] each query has its own time execution,
and at any given moment only one query can be 
executed.

The idea: 
  Sort the array (integral prospective as its offset) and do calculation.


        queries = [3, 2, 1, 2, 6]
        expected = 17

"""


def minimumWaitingTime(queries):
	# 1, 2, 2, 3, 6
	# 0 + ((0) + 1) + ((1) + 2) + ((3) + 2) + ((5) + 3)
	# 0 + 1 + 3 + 5 + 8 = 17
	
  queries.sort()
	min_wait_time = 0	# 8
	prev_result = 0
	for idx in range(1, len(queries)): # 4
		min_wait_time += (prev_result + queries[idx-1])
		prev_result = (prev_result + queries[idx-1])
	return min_wait_time
