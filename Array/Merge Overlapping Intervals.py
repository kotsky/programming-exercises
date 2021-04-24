def mergeOverlappingIntervals(intervals):
	
	if not intervals:
		return [[]]
	
	intervals.sort(key=lambda x: x[0])
	merged_intervals = []
	
	for new_interval in intervals:
		if not merged_intervals:
			merged_intervals.append(new_interval)
			continue
		
		if new_interval[0] > merged_intervals[-1][1]:
			merged_intervals.append(new_interval)
			continue
		else:
			if new_interval[1] > merged_intervals[-1][1]:
				merged_intervals[-1][1] = new_interval[1]
	
    return merged_intervals

