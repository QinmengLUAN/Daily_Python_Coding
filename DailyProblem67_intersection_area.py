"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given two rectangles, find the area of intersection.

Here's some starter code and a starter example:

class Rectangle():
  def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
    self.min_x = min_x
    self.min_y = min_y
    self.max_x = max_x
    self.max_y = max_y

def intersection_area(rect1, rect2):
  # Fill this in.

#  BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2
"""
class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

def intersection_area(rect1, rect2):
    # a1 = abs(rec1[0] - rec1[2]) * abs(rec1[1] - rec1[3])
    # a2 = abs(rec2[0] - rec2[2]) * abs(rec2[1] - rec2[3])

    x_dis = min(rect1[2], rect2[2]) - max(rect1[0], rect2[0])
    y_dis = min(rect1[3], rect2[3]) - max(rect1[1], rect2[1])

    if x_dis > 0 and y_dis > 0:
        return x_dis * y_dis
    return 0

#  BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2