"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
You can assume there will be no arrays, and all keys will be strings.

Here's some starter code:

def flatten_dictionary(d):
  # Fill this in.

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
"""
# Method 1: backtracking
def flatten_dictionary1(d):
    nd = {}
    helper(d, nd, [])
    return nd

def helper(dd, nd, pre):
    for k, v in dd.items():
        pre.append(k)

        if not isinstance(v, dict):
            nd['.'.join(pre)] = v
        else:
            helper(v, nd, pre)

        pre.pop()

# Method 2: recursion
def flatten_dictionary(d):
    for k, v in list(d.items()):
        if isinstance(v, dict):
            del d[k]
            for nk, nv in flatten_dictionary(v).items():
                d[k + '.' + nk] = nv
    return d

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': {'g':4}
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}