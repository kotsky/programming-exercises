'''
You are given disks with its [weight, depth, height].
Return subarrays, which create the max possible height.
Those subarrays must be in order of increasing [weight, depth, height].

Input: [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]),
Output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
'''

def diskStacking(disks):
    heights = [0] * len(disks)  # contains max height at each disks index

    # back_track contains reference to the subarray,
    # which was used to make a max height
    # at respective idx
    back_track = [None] * len(disks)

    # step 1: ful fil heights and back_track
    # with max height info at each idx
	
    # to do sort to ensure subarrays in order of heights  
    # to have a possibility to compare only from 
    # the bottom side as a base
    disks.sort(key=lambda disk: disk[2])

    for i in range(len(disks)):
        base = disks[i]
        local_high = base[2]
        reference = None
        for j in range(i - 1, -1, -1):
            tops = disks[j]
            if compare(base, tops):
                if base[2] + heights[j] > local_high:
                    local_high = base[2] + heights[j]
                    reference = j
        back_track[i] = reference
        heights[i] = local_high

    # step 2: find max hight and its idx
    maxi_high = 0
    maxi_high_idx = -1
    for i in range(len(heights)):
        if maxi_high < heights[i]:
            maxi_high = heights[i]
            maxi_high_idx = i

    if maxi_high_idx == -1:
        return []

    # step 3: back track of elements
    # to build array answer

    disks_stack = [disks[maxi_high_idx].copy()]
    pointer = back_track[maxi_high_idx]
    while pointer is not None:
        disks_stack.append(disks[pointer])
        pointer = back_track[pointer]

    return disks_stack[::-1]


def compare(arrayBot, arrayTop):
    for idx in range(len(arrayBot)):
        if arrayBot[idx] <= arrayTop[idx]:
            return False
    return True
