'''Permutation Generator

Iterative solution to generate permutation

Example:

  array = [1, 2, 3, 4]
  heap_permutation_generation(array, len(array))

'''

def heap_permutation_generation(array, n):
    
    def _swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    n = len(array)
    c = [0] * n
    i = 0

    print(array)

    while i < n:
        if c[i] < i:
            if (i & 1) is False:
                _swap(array, 0, i)
            else:
                _swap(array, c[i], i)
            print(array)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
            
