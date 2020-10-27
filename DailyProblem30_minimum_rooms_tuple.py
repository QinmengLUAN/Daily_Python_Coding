"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""
def minimum_rooms(lectures):   
    if len(lectures) < 2:
        return len(lectures)
    new_tuple = []
    for i in range(len(lectures)):
        new_tuple.append((lectures[i][0], 1))
        new_tuple.append((lectures[i][1], -1))
    new_tuple.sort()

    res, tmp = 0, 0
    for k in range(len(new_tuple)):
        tmp += new_tuple[k][1]
        res = max(tmp, res)
    return res

lectures = [(10,20), (15,25), (25,30), (20,30)]
print('Max Rooms', minimum_rooms(lectures))