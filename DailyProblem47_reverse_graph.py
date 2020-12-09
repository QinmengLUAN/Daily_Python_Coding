"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a directed graph, reverse the directed graph so all directed edges are reversed.

Example:
Input:
A -> B, B -> C, A ->C

Output:
B->A, C -> B, C -> A
Here's a starting point:

from collections import defaultdict

class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
  # Fill this in.

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
  print(val.adjacent)
# []
# ['a', 'b']
# ['a']
"""
# Algo: 
# 1. create a new_adj dictionary to store new_adj[node] with new_adjacents
# 2. replace the node.adjcent by new_adj[node]
# 3. create an empty [] if has no new_adjcents

from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

    def __repr__(self):
        return self.value
 

def reverse_graph(graph):
    # Fill this in.
    new_adj = {}
    for val, node in graph.items():
        for adj in node.adjacent:
            if adj not in new_adj:
                new_adj[adj] = []
            new_adj[adj].append(node)

    for val, node in graph.items():
        node.adjacent = new_adj[node] if node in new_adj else []
    return graph



a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for key, val in reverse_graph(graph).items():
  print(key, val.adjacent)
# []
# ['a', 'b']
# ['a']