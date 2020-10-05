"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

Here's a starting point:

def merge(intervals):
  # Fill this in.
  
print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]
"""
def merge(intervals):
    intervals.sort()
    res = []
    if len(intervals) == 0:
        return res
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            res.append((start, end))
            start, end = intervals[i][0], intervals[i][1]
        elif intervals[i][1] > end:
            end = intervals[i][1]
    res.append((start, end))
    return res
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]