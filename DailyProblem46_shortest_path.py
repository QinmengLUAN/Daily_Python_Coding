"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), return the shortest possible file path (Eliminate all the '..' and '.').

Example
Input: '/Users/Joma/Documents/../Desktop/./../'
Output: '/Users/Joma/'
def shortest_path(file_path):
  # Fill this in.

print shortest_path('/Users/Joma/Documents/../Desktop/./../')
# /Users/Joma/
"""
# Rules to simplify the directory path (Unix like)
# https://www.geeksforgeeks.org/simplify-directory-path-unix-like/

def shortest_path(file_path):
    st, rev_st = [], []
    # every string starts from root directory
    res = "/"

    length = len(file_path)
    i = 0

    # Step 1: pre-process the strings and store them in a stack
    while i < length:
        # create an empty temporary curr_str
        curr_str = ""
        # skip all the multiple '/'
        while (i < length and file_path[i] == "/"):
            i += 1

        while (i < length and file_path[i] != "/"):
            curr_str += file_path[i]
            i += 1

        # if dir has ".." just pop the topmost element 
        # if the stack is not empty, otherwise ignore. 
        if curr_str == "..": 
            if len(st) > 1: 
                st.pop()

        # if dir has "." then simply continue 
        # with the process. 
        elif curr_str == '.': 
            continue

        # pushes the curr_str into stack if it is not empty
        elif len(curr_str) > 0: 
            st.append(curr_str)
        i += 1

    # Step 2: use another stack to store reversed strings, 
    # pop the elements in rev_st to generate the final result
    while len(st) > 0:
        rev_st.append(st.pop())

    while len(rev_st) > 0:
        tmp = rev_st.pop()
        if len(rev_st) > 0:
            res += (tmp + "/")
        else:
            res += tmp
    return res

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/