"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hash = dict()
        def helper(node):
            val = node.val
            if val in hash:
                return
            duplicated = Node(val)
            hash[val] = duplicated
            for neighbor in node.neighbors:
                if not neighbor.val in hash:
                    helper(neighbor)
            duplicated.neighbors = [hash[n.val] for n in node.neighbors]
            return duplicated
        return helper(node)

        

        