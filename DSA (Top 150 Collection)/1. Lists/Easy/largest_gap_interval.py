"""
https://www.geeksforgeeks.org/problems/largest-gap/1?page=1&category=Arrays&difficulty=Easy&sortBy=accuracy
Here we are going to find the largest time period where car is not moving.
The key to solve this problem is to sort the intervals based on their sort so that,
we handle the edge-cases of future overlap and miscalculation of gap.
Once that is done, then it remains a single comparison of current start and prev end.
"""

def maximum_gap(start: list, end: list) -> int:
    intervals = list(zip(start, end))
    intervals.sort(key=lambda x: x[0])
    tracking_end = intervals[0][1]
    gap = 0

    for interval in intervals[1:]:
        if interval[0] > tracking_end:
            gap = max(gap, interval[0] - tracking_end)
        tracking_end = max(tracking_end, interval[1])

    return gap

# s = [20, 18, 4]
# e = [25, 20, 15]

# s = [3, 1]
# e = [5, 5]

# s = [20, 30, 48]
# e = [25, 40, 65]

s = [0, 10, 5]
e = [1, 11, 6]
print(maximum_gap(s, e))