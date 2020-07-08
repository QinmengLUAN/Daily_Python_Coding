"""
207. Course Schedule
Medium: Graph

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        cnext = {}
        npre = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][1] in cnext:
                cnext[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                cnext[prerequisites[i][1]] = [prerequisites[i][0]]
            
            if prerequisites[i][0] not in npre:
                npre[prerequisites[i][0]] = 1
            else:
                npre[prerequisites[i][0]] += 1
            if prerequisites[i][1] not in npre:
                npre[prerequisites[i][1]] = 0
        print(cnext)
        print(npre)
        if len(npre) == 0 and numCourses == 1:
            return True
        dq = deque([i for i in npre if npre[i] == 0]) 
        print(dq)
        finished = 0
        while len(dq) > 0:
            c = dq.popleft()
            finished += 1
            # print(finished)
            print(cnext, npre)
            if c not in cnext:
                continue 
            for cn in cnext[c]:
                npre[cn] -= 1
                if npre[cn] == 0:
                    dq.append(cn)
        return finished == len(npre)

numCourses = 4
prerequisites = [[3,0],[0,1]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))