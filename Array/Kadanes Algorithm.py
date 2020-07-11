def kadanesAlgorithm(array):
	suma = array[0]
	local_suma = array[0]
	
	for i in range(1, len(array)):	
		num = array[i]
		local_suma = max(local_suma + num, num)		
		suma = max(local_suma, suma)
			
	return suma
