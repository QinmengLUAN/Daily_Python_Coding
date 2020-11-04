"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
  # Fill this in.

print calcAngle(3, 30)
# 75
print calcAngle(12, 30)
# 165
"""
def calcAngle(h, m):
    diff = abs(h * 30 + m//2 - m * 6)
    return diff if diff <=180 else 360 - diff

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165