"""
https://leetcode.com/discuss/interview-question/363120/Goldman-Sachs-or-OA-2019-or-Spiral-Matrix
"""
def spiralOrder(self, matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2: # handle 1,1,1,1 case
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1
    
    def check_prime(n):
        r = int(n**0.5)
        for i in range(2, r+1):
            if n % i == 0:
                return False
        return True

    if not matrix: return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            k = matrix[r][c]
            if check_prime(k):
                ans.append(k)
        r1 += 1; r2 -= 1
        c1 += 1; c2 -= 1
    return ans