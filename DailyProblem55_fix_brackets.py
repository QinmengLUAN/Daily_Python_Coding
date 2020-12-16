"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.

Example:
Input: '(()()'
Output: 1
Explanation:

The fixed string could either be ()() by deleting the first bracket, or (()()) by adding a bracket. These are not the only ways of fixing the string, there are many other ways by adding it in different positions!


Here's some code to start with:

def fix_brackets(s):
  # Fill this in.

print fix_brackets('(()()')
# 1
"""
def fix_brackets(s):
    st, st2 = [], []
    for i in range(len(s)):
        st.append(s[i])

    st2.append(st.pop())
    while len(st) > 0:
        if len(st2) > 0 and st[-1] == '(' and st2[-1] == ')':
            st.pop()
            st2.pop()
        else:
            st2.append(st.pop())
    return len(st2)

print(fix_brackets('(()()'))
# 1
print(fix_brackets('(('))
# 2
print(fix_brackets('(())'))
# 0