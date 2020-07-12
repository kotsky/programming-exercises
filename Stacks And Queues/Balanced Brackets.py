'''
"[(s)s1{}][]" => True
"{(}]" or "((())" => False
'''

# O(N) TS
def balancedBrackets(string):
    stack = []
	openElements = "([{"
	closeElements = ")]}"
	matching = {")" : "(", "]" : "[", "}" : "{"}
	
	for char in string:
		if char in openElements:
			stack.append(char)
		elif char in closeElements:
			if len(stack) == 0:
				return False
			if stack[-1] == matching[char]:
				stack.pop()
			else:
				return False
	return True if len(stack) == 0 else False
  
'''
Version 2

# O(N) TS
def balancedBrackets(string):
    stack = StackConstructor()
	
	for i in range(len(string)):
		if openElements(string[i]) >= 0:
			stack.push(string[i])
		elif closeElements(string[i]) >= 0:
			if stack.peek() != None and closeElements(string[i]) == openElements(stack.peek()):
                stack.pop()
            else:
                return False
    return False if len(stack.stack) > 1 else True


def openElements(bracket):
	LUT = ['(', '[', '{']
	index = -1
	for i in range(len(LUT)):
		if bracket == LUT[i]:
			index = i
			break
	return index

def closeElements(bracket):
	LUT = [')', ']', '}']
	index = -1
	for i in range(len(LUT)):
		if bracket == LUT[i]:
			index = i
			break
	return index

class StackConstructor(): #push, pop, peek
	def __init__(self):
		self.stack = [None]
	
	def peek(self):
		return self.stack[-1]
	
	def pop(self):
		self.stack.pop()
	
	def push(self, value):
		self.stack.append(value)
    
'''
	
