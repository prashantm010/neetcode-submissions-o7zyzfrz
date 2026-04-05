"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    mp = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        if node in self.mp:
            return self.mp[node]
        cp = Node(node.val)
        self.mp[node] = cp
        for i in node.neighbors:
            cp.neighbors.append(self.cloneGraph(i))
        return cp
            
        