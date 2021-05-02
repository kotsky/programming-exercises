'''
https://www.algoexpert.io/questions/Tandem%20Bicycle
'''

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
  redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=fastest)
	speed = 0
	for tandem_idx in range(len(redShirtSpeeds)):
		red_guy = redShirtSpeeds[tandem_idx]
		blue_guy = blueShirtSpeeds[tandem_idx]
		speed += max(red_guy, blue_guy)
	return speed
