'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
'''

# O(R^2*C) Time / O(C * R) Space (if not to del old hashes)
class Solution:
  # Solution from Q560: to count subarray, which has sum = target (k) in O(N) Time
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:    return 0
        counter = collections.defaultdict(int)
        counter[0] = 1
        cumsum = 0
        ans = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum-k in counter:
                ans += counter[cumsum-k]
            counter[cumsum] += 1
        return ans
    
    # The idea here is to check line by line with using subarraySum() method
    # with accumulation of matrix sums
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
         
        R,C = len(matrix),len(matrix[0])
        ans = 0
        for r0 in range(R):
            vec = [0] * C
            for r1 in range(r0,R):
                for c0 in range(C):
                    vec[c0] += matrix[r1][c0]
                #find how many subarray sum to target in each flattened matrix
                ans += self.subarraySum(vec,target)
        return ans
        
'''
  # O(R^2 * C^2) Time / O(R^3 * C^3) Space
    def numSubmatrixSumTarget1(self, matrix, target):
        
        count_of_submatrices = 0
        precomp = precomputation(matrix)
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                count_of_submatrices += targetSumsInSubmatrix(matrix, precomp, r, c, target)
        return count_of_submatrices
    
    
def targetSumsInSubmatrix(matrix, precomp, start_r, start_c, target):
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    for end_c in range(start_c, col):
        local_matrix_sum = 0
        flag = False
        for end_r in range(start_r, row):
            flag = False
            key = createKey(end_r, end_r, start_c, end_c)
            local_matrix_sum += precomp[key]
            if local_matrix_sum == target:
                count += 1
                flag = True
        if local_matrix_sum == target and not flag:
            count += 1
    return count

def precomputation(matrix):
    table = {}
    row = len(matrix)
    col = len(matrix[0])

    for r in range(row):
        for start_c in range(col):
            start_c_sum = 0
            for end_c in range(start_c, col):
                key = createKey(r, r, start_c, end_c)
                start_c_sum += matrix[r][end_c]
                table[key] = start_c_sum

    # for c in range(col):
    #     for start_r in range(row):
    #         start_r_sum = 0
    #         for end_r in range(start_r, row):
    #             key = createKey(start_r, end_r, c, c)
    #             start_r_sum += matrix[end_r][c]
    #             table[key] = start_r_sum

    return table

def createKey(start_x, end_x, start_y, end_y):
    return 'x'+str(start_x) + '|' + str(end_x) + '||' + 'y'+str(start_y) + '|' + str(end_y)
'''
        
