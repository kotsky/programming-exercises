"""

k - workers > 0 => each of can complete only 2 tasks.
len(tasks) = 2k

Return list of tasks for each worker to be completed in min overall time.

The idea:
  Sort and track tasks' indexes, and grab min-max tasks.

"""


def taskAssignment(k, tasks):
  sorted_tasks, tasks_indexes = sort_and_track(tasks)
	return build_tasks_order(sorted_tasks, tasks_indexes, k)

def sort_and_track(tasks):
	tasks_indexes = [x for x in range(len(tasks))]
	buble_sort(tasks, tasks_indexes)
	return tasks, tasks_indexes

def buble_sort(tasks, tasks_indexes):
	did_we_do_swap = True
	while did_we_do_swap:
		did_we_do_swap = False
		for i in range(1,len(tasks)):
			if tasks[i-1] > tasks[i]:
				swap(tasks, i)
				swap(tasks_indexes, i)
				did_we_do_swap = True
	return tasks, tasks_indexes

def swap(array, idx):
	array[idx], array[idx-1] = array[idx-1], array[idx]
		
def build_tasks_order(sorted_tasks, tasks_indexes, k):
	tasks_order = []
	for _k in range(k):
		task1 = tasks_indexes[_k]
		task2 = tasks_indexes[-1-_k]
		tasks_order.append([task1, task2])
	return tasks_order
