'''

You have a schedule [from_time, to_time] of students, who needs laptops for their work.
Find out, how many min required laptops you need.

schedule = [[0, 5], [6, 10], [2, 3], [11, 20], [1, 3], [0, 2]]
print(laptopRentals(schedule))

Idea:

V1: create 2 arrays: start times and end times. Sort them and go through started times and check,
how many laptops you need every start times and did old laptop is free from end times?

V2: do sort and track, if prev laptop is free then -1, if no - add 1 to total number of laptops.
Use heap for efficient data storage of time info.
'''

# Version 1
def laptopRentals(times):
	start_times = []
	end_times = []
	
	for time in times:
		start_times.append(time[0])
		end_times.append(time[1])
	
	start_times.sort()
	end_times.sort()
	
	max_laptops = 0
	current_laptops = 0
	i = 0
	j = 0
	while i < len(start_times):
		start = start_times[i]
		end = end_times[j]
		if start < end:
			current_laptops += 1
			i += 1
		else:
			current_laptops -= 1
			j += 1
		max_laptops = max(max_laptops, current_laptops)
	return max_laptops

'''
def laptopRentals(schedule):
    if not schedule:
        return 0

    schedule.sort()

    max_laptops_global = 1
    current_laptop_in_use = 1
    laptops_info = MinHeap([])
    laptops_info.insert(schedule[0][1])

    for idx in range(1, len(schedule)):
        start_time, end_time = schedule[idx]

        if end_time - start_time <= 0:
            continue

        # get info when earliest laptop is free
        earliest_free_laptop_at = laptops_info.peek()

        # check if start time is greater
        # than the earliest free laptop, then
        # add needed laptop to use
        if start_time < earliest_free_laptop_at:
            current_laptop_in_use += 0
        else:
            current_laptop_in_use -= 1
			laptops_info.pop()

        # add info about current using laptop
        laptops_info.insert(end_time)
        current_laptop_in_use += 1
        max_laptops_global = max(max_laptops_global, current_laptop_in_use)
    return max_laptops_global


class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap(self.heap)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index)
            child_index -= 2
            parent_index = (child_index - 1) // 2

    def head(self):
        return self.heap[0]

    def is_empty(self):
        return self.length() == 0

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, -1)
            value = self.heap.pop()
            self.siftDown(idx)
        return value

    def length(self):
        return len(self.heap)

    def siftDown(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] <= self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] > self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] > self.heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def siftUp(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        parent_index = (start_index - 1) // 2
        while parent_index >= 0:
            if self.heap[parent_index] > self.heap[start_index]:
                self.swap(start_index, parent_index)
                start_index = parent_index
                parent_index = (start_index - 1) // 2
            else:
                break

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def printHeap(self):
        for num in self.heap:
            print(num, end=' ')
        print('', end='\n')
		
class MaxHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap(self.heap)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index)
            child_index -= 2
            parent_index = (child_index - 1) // 2

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def siftDown(self, start_index):
		if start_index < 0:
			start_index = len(self.heap) + start_index
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] >= self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] < self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def siftUp(self, idx):
		if idx < 0:
			idx = len(self.heap) + idx
        idx_parent = (idx - 1) // 2
        while idx_parent >= 0:
            if self.heap[idx] > self.heap[idx_parent]:
                self.swap(idx, idx_parent)
                idx = idx_parent
                idx_parent = (idx - 1) // 2
            else:
                break

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, -1)
            value = self.heap.pop()
            self.siftDown(idx)
        return value

    def length(self):
        return len(self.heap)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def printHeap(self):
        for num in self.heap:
            if type(num) == int:
                print(num, end=' ')
        print('', end='\n')

'''
