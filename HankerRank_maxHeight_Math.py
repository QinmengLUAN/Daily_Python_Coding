"""
Your company is designing a dam to be built across a stream to create a small lake. To reduce materials cost, it will be made of one or more concrete walls with mud packed in between them. Determine the maximum height of the mud segments in the dam with the following restrictions:

One unit width of the gap between walls will contain one segment of packed mud
The height of mud in a segment cannot exceed 1 unit more than an adjacent wall or mud segment.

Given the placement of a number of walls and their heights, determine the maximum height of a mud segment that can be built. If no mud segment can be built, return 0.

For example, there are n = 4 walls at wallPositions = [1, 2, 4, 7] with wallHeights = [4, 6, 8, 11].

There is no space between the first two walls.
Between positions 2 and 4, there is one unit open for mud. Heights of the surrounding walls are 6 and 8, so the maximum height of mud is 6 + 1 = 7.
Between positions 4 and 7 there are two units. The heights of surrounding walls are 8 and 11.
The maximum height mud segment next to the wall of height 8 is 9.
The maximum height mud next to a mud segment of height 9 and a wall of height 11 is 10.
Overall, mud segment heights are 7, 9 and 10, and the maximum height is 10.

Function Description

Complete the function maxHeight in the editor below. The function must return an integer, the maximum height mud segment that can be built.

maxHeight has the following parameter(s):

wallPositions[wallPositions[0],...wallPositions[n-1]]:  an array of integers

wallHeights[wallHeights[0],...wallHeights[n-1]]:  an array of integers
Constraints

1 < n ≤ 105
1 ≤ wallPositions[i] ≤ 109 (where 0 ≤ i < n)
1 ≤ wallHeights[i] ≤ 109 (where 0 ≤ i < n)
"""
def maxHeight(wallPositions, wallHeights):
    res = 0
    for i in range(len(wallPositions) - 1):
        res = max(res, helper(wallPositions[i], wallHeights[i], wallPositions[i+1], wallHeights[i+1]))
    return res

def helper(p1, h1, p2, h2):
    h = min(h1, h2)
    dh = abs(h1 - h2)
    dp = abs(p1 - p2)
    if dp < dh:
        return h + dp
    else:
        h += dh
        h += (dp - dh + 1) // 2
    return h

print(maxHeight([1,3],[1,2]))

