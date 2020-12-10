"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Version numbers are strings that are used to identify unique states of software products. A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent a hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the latest version number. Your code should do the following:
If version1 > version2 return 1.
If version1 < version2 return -1.
Otherwise return 0.

Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not start or end with dots. Unspecified level revision numbers default to 0.

Example:
Input: 
version1 = "1.0.33"
version2 = "1.0.27"
Output: 1 
#version1 > version2

Input:
version1 = "0.1"
version2 = "1.1"
Output: -1
#version1 < version2

Input: 
version1 = "1.01"
version2 = "1.001"
Output: 0
#ignore leading zeroes, 01 and 001 represent the same number. 

Input:
version1 = "1.0"
version2 = "1.0.0"
Output: 0
#version1 does not have a 3rd level revision number, which
defaults to "0"
Here's a starting point

class Solution:
  def compareVersion(self, version1, version2):
    # Fill this in.

version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
"""
# Link: https://www.geeksforgeeks.org/compare-two-version-numbers/
class Solution:
    def compareVersion(self, version1, version2):
        # This will split both the versions by '.'
        v1, v2 = version1.split("."), version2.split(".")
        m, n = len(v1), len(v2)

        # converts to integer from string 
        v1 = [int(i) for i in v1]
        v2 = [int(j) for j in v2]

        # compares which list is bigger and fills  
        # smaller list with zero (for unequal delimeters) 
        if m > n: 
            for i in range(n, m): 
                v2.append(0) 
        elif n > m: 
            for i in range(m, n): 
                v1.append(0)

        # returns 1 if version 1 is bigger and -1 if 
        # version 2 is bigger and 0 if equal 
        for i in range(len(v1)): 
            if v1[i] > v2[i]: 
                return 1
            elif v2[i] > v1[i]: 
                return -1
        return 0


version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
version1 = "1.0"
version2 = "1.0.0"
print(Solution().compareVersion(version1, version2))
# 0
version1 = "0.1"
version2 = "1.1"
print(Solution().compareVersion(version1, version2))
# -1
version1 = "1.01"
version2 = "1.001"
print(Solution().compareVersion(version1, version2))
# 0