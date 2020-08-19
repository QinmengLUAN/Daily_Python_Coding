"""
56. Merge Intervals
Medium: Array

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        if len(intervals) == 0:
            return res
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(intervals[i][1], end)
        res.append([start, end])
        return res
