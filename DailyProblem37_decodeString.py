"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

Your starting point:

def decodeString(s):
  # Fill this in.

print decodeString('2[a2[b]c]')
# abbcabbc
"""
def decodeString(s):
    curNum = 0
    curString = ""
    stack = []

    for st in s:
        if st == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ""
            curNum = 0

        elif st == ']':
            num = stack.pop()
            preString = stack.pop()
            curString = preString + num * curString 

        elif st.isdigit():
            curNum = curNum * 10 + int(st)
        else:
            curString += st
    return curString

print(decodeString('2[a2[b]c]'))
# abbcabbc