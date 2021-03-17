# Time complexity: O(n * len(sprints)) worst
# Space complexity: O(n)

# Its task in additional_data/sprints_task.png

def get_most_visited(n: int, sprints: list) -> int:
    """

    :param n: number of sprints
    :param sprints: sprints intervals
    :return: spot of max visited, else -1
    """

    def _assign_visit_to_place(start: int, end: int, track: list) -> list:
        if start > end:
            start, end = end, start

        while end >= start:
            track[start-1] += 1
            start += 1

        return track

    def _return_first_min_place(track: list) -> int:
        most_visited_count = float("-inf")
        most_visited_place = -1
        for i in range(len(track)):
            if most_visited_count < track[i]:
                most_visited_count = track[i]
                most_visited_place = i + 1
        return most_visited_place

    if not n or not sprints:
        return -1

    # let's create a road to run for a guy
    track_run = [0] * n
    # each index+1 is a label for a place

    for idx in range(len(sprints) - 1):
        start_point = sprints[idx]
        end_point = sprints[idx+1]

        if start_point > n or end_point > n:
            return -1

        # let's the guy run track from the start to the end
        track_run = _assign_visit_to_place(start_point, end_point, track_run)

    return _return_first_min_place(track_run)


n = 5
sprints = [2, 4, 1, 3]
print("The most visited spot is {}".format(get_most_visited(n, sprints)))

n = 5
sprints = [2, 4, 6, 3]
print("The most visited spot is {}".format(get_most_visited(n, sprints)))

n = 3
sprints = [2, 4, 1, 3]
print("The most visited spot is {}".format(get_most_visited(n, sprints)))
