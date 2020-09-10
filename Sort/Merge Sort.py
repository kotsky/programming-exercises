# Merge Sort Algorythms
# O(N*log(N)) T / O(N) S

def mergeSort(array):
    if not len(array) or len(array) <= 1:
        return array
    else:
        merge_array = array
        additional_array = array.copy()
        mergeSubarrays(merge_array, additional_array, 0, len(array) - 1)
        return merge_array


def mergeSubarrays(merge_array, additional_array, start_idx, end_idx):
    if end_idx - start_idx < 1:
        return
    middle_idx = (end_idx + start_idx) // 2
    mergeSubarrays(additional_array, merge_array, start_idx, middle_idx)
    mergeSubarrays(additional_array, merge_array, middle_idx + 1, end_idx)
    doMerge(merge_array, additional_array, start_idx, middle_idx + 1, end_idx)


def doMerge(merge_array, additional_array, start_one, start_two, end_idx):
    p1 = start_one
    p2 = start_two
    p0 = p1
    while p1 < start_two and p2 <= end_idx:
        if additional_array[p1] > additional_array[p2]:
            merge_array[p0] = additional_array[p2]
            p2 += 1
        else:
            merge_array[p0] = additional_array[p1]
            p1 += 1
        p0 += 1
    while p1 < start_two:
        merge_array[p0] = additional_array[p1]
        p1 += 1
        p0 += 1
    while p2 <= end_idx:
        merge_array[p0] = additional_array[p2]
        p2 += 1
        p0 += 1
