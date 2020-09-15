import sys

# Type 1: reading a file
f = open('readfilesPractice.txt', 'r')
f_new = open('readfilesPracticeNew.txt', 'w')

# Type 2: read from input
src = sys.stdin

for line in src:
    tmp = [t for t in line.split()]
    for i in range(len(tmp)):
        tmp[i] = tmp[i][0].upper() + tmp[i][1:]
    print(tmp)
    f_new.write(" ".join(tmp))
    # print(line)
f_new.close()
f.close()