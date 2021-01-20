# 
# Your previous Plain Text content is preserved below:
# 
# Given N tasks each associated with a pair of positive integers [X,Y] where X is the start time and Y is the finish time. 
A task runs on a machine. On one machine, only one task can run at a time. 
What is the minimum number of machines required to handle those N tasks so that no task has to wait?
# 
# Input: {[1,4]} => [1,4] is one task
# Ans: 1
# Input: {[1,4], [4,6]}
# Ans: 1

# Input: {     [1,3],
#              [2,5],
#              [5,8]
# } => 3 tasks


# O(N^2) Time / O(1) Space 

def min_number_machines_required(tasks):
    
    tasks.sort()
    
    max_machine = 0

    for current_i_of_task in range(len(tasks)): 

        current_task_start_time = tasks[current_i_of_task][0]    

        if current_i_of_task == 0:
            machines = 1
        else:
            if tasks[current_i_of_task-1][1] > current_task_start_time:    
                machines += 1

        for i in range(current_i_of_task-2, -1, -1):  
            if tasks[i][1] < current_task_start_time:     
                machines -= 1

        max_machine = max(max_machine, machines)
        
    return max_machine


tasks = [[0,4], [1,2], [2,3], [3, 6], [3, 9], [0, 3]]

print(min_number_machines_required(tasks))

