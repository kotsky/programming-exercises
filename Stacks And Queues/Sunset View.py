"""
Which building can see the sunset from "EAST" or "WEST"?
Given array - buildings' height
Output - buildings' idx, who can see the sunset.
Building can see the sunset in case all building before are smaller.
"""


def sunsetViews(buildings, direction):
	
	def _check_building(condition):
		if idx == condition:
			sunset_buildings.append(idx)
		else:
			if buildings[idx] > buildings[sunset_buildings[-1]]:
				sunset_buildings.append(idx)
    
	if not buildings:
    	return []

	sunset_buildings = []
	
	if direction == "EAST":
		for idx in reversed(range(len(buildings))):
			_check_building(len(buildings)-1)
			
		sunset_buildings = sunset_buildings[::-1]
	else:
		for idx in range(len(buildings)):
			_check_building(0)
	
	return sunset_buildings
