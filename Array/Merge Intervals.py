'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''




O(N) solution

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(intervals, new_interval):
        A = intervals
        st = []
        e = []
        N = len(intervals)
        b0 = new_interval[0]
        b1 = new_interval[1]

        for i in range(N):
            if i == 0:
                if b0 <= A[i][0]:
                    st.append(b0)
                if b1 <= A[i][1]:
                    e.append(b1)
            else:
                if b0 < A[i][0] and b0 >= A[i - 1][0]:
                    st.append(b0)
                if b1 < A[i][1] and b1 >= A[i - 1][1]:
                    e.append(b1)

            st.append(A[i][0])
            e.append(A[i][1])

        if b0 >= A[i][0]:
            st.append(b0)
        if b1 >= A[i][1]:
            e.append(b1)

        res = []
        local_st = st[0]
        i = 0
        while i < N:
            if e[i] < st[i + 1]:
                res.append([local_st, e[i]])
                local_st = st[i + 1]
            else:
                local_st = min(local_st, st[i])

            i += 1
            if i == N:
                res.append([local_st, e[i]])

        return res



A = [ [1, 2], [3, 6] ]
B= [8, 19]

print(Solution.insert(A, B))
