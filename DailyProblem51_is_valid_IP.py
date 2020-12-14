"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']
def ip_addresses(s, ip_parts=[]):
  # Fill this in.

print ip_addresses('1592551013')
# ['159.255.101.3', '159.255.10.13']
"""
# First method: recursion, back-tracking
def ip_addresses(s, ip_parts=[]):
    helper(s, 0, [], ip_parts)
    return ip_parts

def helper(s, idx, curr, ip_parts):
    if len(curr) == 4 and idx == len(s):
        ip_parts.append('.'.join(curr))

    if idx >= len(s) or len(curr) >=4:
        return

    if s[idx] == '0':
        curr.append('0')
        helper(s, idx+1, curr, ip_parts)
        curr.pop()
    else:
        for next_idx in range(idx+1, idx+4):
            num = int(s[idx:next_idx])
            if num > 255:
                continue
            curr.append(str(num))
            helper(s, next_idx, curr, ip_parts)
            curr.pop()


# Second way, for loops to check all possibilities
def ip_addresses2(s, ip_parts=[]):
    sz = len(s)
    if sz > 12:
        return ip_parts

    snew = s
    # Generating different combinations. 
    for i in range(1, sz - 2): 
        for j in range(i + 1, sz - 1): 
            for k in range(j + 1, sz): 
                snew = snew[:k] + "." + snew[k:] 
                snew = snew[:j] + "." + snew[j:] 
                snew = snew[:i] + "." + snew[i:] 
                print(snew)
                # Check for the validity of combination 
                if is_valid(snew): 
                    ip_parts.append(snew)                   
                snew = s 
                  
    return ip_parts 

def is_valid(ip):
    ip = ip.split(".")

    for i in ip:
        if (len(i) > 3 or int(i) > 255 or int(i) < 0):
            return False
        if len(i) > 1 and int(i) == 0: 
            return False
        if (len(i) > 1 and int(i) != 0 and i[0] == '0'):
            return False
    return True

print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']