"""
Hi, here's your problem today. This problem was recently asked by Apple:

In many spreadsheet applications, the columns are marked with letters. 
From the 1st to the 26th column the letters are A to Z. 
Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

Given a number n, find the n-th column name.

def column_name(n):
  # Fill this in.

print column_name(26)
print column_name(27)
print column_name(28)
# Z
# AA
# AB
"""
def column_name(n):
    res = []
    while n > 0:
        rem = n % 26
        if rem == 0:
            res.append('Z')
            n = (n // 26) - 1
        else:
            res.append(chr(rem - 1 + ord('A')))
            n = n // 26
    # print(res)
    res.reverse()
    return "".join(res)


print(column_name(26))
print(column_name(27))
print(column_name(28))
# Z
# AA
# AB