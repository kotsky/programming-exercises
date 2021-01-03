'''Longest Balanced Substring

Count max length of balanced substring of brackets.
Balanced means (()) or ()(), but not )( or ))).

3 ideas:
1. Travers to the 1) right and 2) left and check
'(' and ')' according to the direction of traversing. 
Once quantity of '(' = to ')' => current_lenth = that amount * 2.
Once quantity of '(' < ')' or '(' > ')' according to direction,
restart counting.

2. Use index_stack to store open brackets indecex and start_idx of 
possible balanced substring as a first element in this index_stack.

3. Check every substring if that substring is balanced.

input:
        string = "((()(()))(((((())((("
output:
        8


'''

# O(N) Time / O(1) Space

def longestBalancedSubstring(string):
	max_length = 0
	current_length = 0
	open_brackets = 0
	close_brackets = 0
	
	# move to the right first 
	for idx in range(len(string)):
		if string[idx] == '(':
			open_brackets += 1
		else:
			close_brackets += 1
			if close_brackets == open_brackets:
				current_length = open_brackets * 2
				max_length = max(max_length, current_length)
			elif close_brackets > open_brackets:
				open_brackets = 0
				close_brackets = 0
				current_length = 0
				
	open_brackets = 0
	close_brackets = 0
	current_length = 0
	# move to the left
	for idx in range(len(string)-1, -1, -1):
		if string[idx] == ')':
			open_brackets += 1
		else:
			close_brackets += 1
			if close_brackets == open_brackets:
				current_length = open_brackets * 2
				max_length = max(max_length, current_length)
			elif close_brackets > open_brackets:
				open_brackets = 0
				close_brackets = 0
				current_length = 0
	return max_length


# # O(N) Time / O(N) Space

# def longestBalancedSubstring(string):
#     stack_idx = [-1]
# 	length = 0
# 	for idx in range(len(string)):
# 		if string[idx] == '(':
# 			stack_idx.append(idx)
# 		else:
# 			stack_idx.pop()
# 			if not len(stack_idx):
# 				stack_idx.append(idx)
# 			else:
# 				length = max(length, idx - stack_idx[-1])
# 	return length


# # O(N^3) Time / O(1) Space

# def longestBalancedSubstring(string):
#     max_length = 0
# 	for start_idx in range(len(string)):
# 		for idx in range(start_idx, len(string)):
# 			if is_balanced(string, start_idx, idx):
# 				max_length = max(max_length, idx-start_idx+1)
# 	return max_length


# def is_balanced(string, start_idx, end_idx):
# 	open_brackets = 0
# 	close_brackets = 0
# 	for idx in range(start_idx, end_idx+1):
# 		open_brackets += 1 if string[idx] == '(' else 0
# 		close_brackets += 1 if string[idx] == ')' else 0
# 		delta = open_brackets - close_brackets
# 		if delta < 0:
# 			return False
# 	return delta == 0
