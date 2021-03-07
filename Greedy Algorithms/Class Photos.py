'''

Find out if one array can cover another one in terms of its values.

'''

# O(N*log(N)) T / O(1) Space
def classPhotos(redShirtHeights, blueShirtHeights):
    # sort method
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	if redShirtHeights[0] == blueShirtHeights[0]:
		return False
	elif redShirtHeights[0] < blueShirtHeights[0]:
		answer = compare_arrays(redShirtHeights, blueShirtHeights)
	else:
		answer = compare_arrays(blueShirtHeights, redShirtHeights)
	return answer

def compare_arrays(array1, array2):
	p = 0
	while p < len(array1):
		if array1[p] >= array2[p]:
			return False
		p += 1
	return True
