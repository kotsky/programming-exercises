

def getNthFib(n):
	
	if n <= 0:
		return None
    
	if n == 1 or n == 2:
		return n-1
	
	num1 = 0
	num2 = 1
	counter = 2
	
	while counter < n:
		num3 = num1 + num2
		num1 = num2
		num2 = num3
		counter += 1
		
	return num3
