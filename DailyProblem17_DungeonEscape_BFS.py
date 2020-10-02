"""
是给一个矩阵，有些点可以走有些点不能走，
返回一条从给定起始点到终点的最短路径，
如果没有的话就返回没有。

两个coding 
第一个从给定start和end之间找shortest path，
input是2D， 有障碍标记为"#"， 可以通过是".", 
output要把shortest path经过的地方.变为* ， return这个2D
"""
    # Till here, the map looks like:
    # S # E     S # E
    # . . .  => 1 2 3
    # . . .     2 3 4

"""
# time complexity O(n*2)
# space complexity O(n*2)
# BFS
"""
import sys
from collections import deque

def _get_adj_pos(r, c, max_r, max_c):
    for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < max_r and 0 <= new_c < max_c:
            yield new_r, new_c

inp = [list(line.strip()) for line in sys.stdin]
# print(inp)
inp = inp[1:]
# print(inp)

max_r, max_c = len(inp), len(inp[0])

# validate input
if max_r <= 0 or max_c <= 0:
    print(inp)

# find S(start point) and E(end point) from map
for r in range(max_r):
    for c in range(max_c):
        if inp[r][c] == 'S':
            start_r, start_c = r, c
        elif inp[r][c] == 'E':
            end_r, end_c = r, c

# BFS
dq = deque()
dq.append((start_r, start_c))
found = False
step = 0
while len(dq) > 0:
    for _ in range(len(dq)):
        r, c = dq.popleft()    
        for new_r, new_c in _get_adj_pos(r, c, max_r, max_c):
            if inp[new_r][new_c] == '.':
                dq.append((new_r, new_c))

                # write the layer number into the map
                inp[new_r][new_c] = str(step + 1)
            elif inp[new_r][new_c] == 'E':
                found = True
                break
    if found:
        break
    else:
        step += 1
    # find route backwards
if found:
    r, c = end_r, end_c
    while step > 0:
        for new_r, new_c in _get_adj_pos(r, c, max_r, max_c):
            if inp[new_r][new_c] == str(step):
                r, c = new_r, new_c
                inp[r][c] = '*'
                break
        step -= 1
# Till here, the map looks like:
# S # E     S # E
# 1 2 3  => * * *
# 2 3 4     2 3 4

# reset map
for r in range(max_r):
    for c in range(max_c):
        if inp[r][c] not in ['.', '#', '*', 'S', 'E']:
            inp[r][c] = '.'
print(["".join(l) for l in inp])

# Till here, the map looks like:
# S # E     S # E
# * * *  => * * *
# 2 3 4     . . .  

# src = ['1', 'S#E','...','...']
# DungeonEscape(src)




