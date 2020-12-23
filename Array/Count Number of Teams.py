"""

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).


Example:
    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

# ============ Solving ===========
# rating[i] < rating[j] < rating[k]
        ->i->j->k
        0,1,2,3,4
array = 2,5,3,4,1

step 0: pre-computation!
    O(N^2) TIme
table_of_next
    2:  (idx_j)   1, 2, 3
    3:  [3]

2 -> 3 -> 4 => += 1

count = 0

O(N^2) Time

for num_i in table_of_next:
    for j in table_of_next[num_i]:
        num_j = array[j]
        if num_j in table_of_next:
            local_count = len(table_of_next[num_j])
            count += local_count

# ==================================
# O(N^3) Time / O(1) Space

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] < array[j]:
            for k in range(j+1, len(array)):
                if array[j] < array[k]:
                    count += 1
# ==================================
"""


def count_teams(num_teams):

    def _build_table_of_next(array):
        table = {}
        # rating[i] < rating[j] <>> rating[k]
        for i in range(len(array)):
            num_i = array[i]
            for j in range(i + 1, len(array)):
                num_j = array[j]
                if num_i < num_j:
                    if num_i not in table:
                        table[num_i] = [j]
                    else:
                        table[num_i].append(j)
        table_storage = [table]
        table = {}
        # rating[i] > rating[j] > rating[k]
        for i in range(len(array)):
            num_i = array[i]
            for j in range(i + 1, len(array)):
                num_j = array[j]
                if num_i > num_j:
                    if num_i not in table:
                        table[num_i] = [j]
                    else:
                        table[num_i].append(j)
        table_storage.append(table)
        return table_storage

    tables = _build_table_of_next(num_teams)
    count = 0

    for table_of_next in tables:    # 2
        for num_i in table_of_next:
            for j in table_of_next[num_i]:
                num_j = num_teams[j]
                if num_j in table_of_next:
                    local_count = len(table_of_next[num_j])
                    count += local_count
    return count


print(count_teams([2, 5, 3, 4, 1]))
