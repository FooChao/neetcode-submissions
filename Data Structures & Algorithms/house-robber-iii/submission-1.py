# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        includeCache = {None: 0}
        excludeCache = {None: 0}
        def best(node, include):
            if include and node in includeCache:
                return includeCache[node]
            if not include and node in excludeCache:
                return excludeCache[node]
            if include:
                includeCache[node] = node.val + best(node.left, False) + best(node.right, False)
                return includeCache[node]
            excludeCache[node] = (              
                max(best(node.left, True), best(node.left, False)) 
                + max(best(node.right, True), best(node.right, False))
            )
            return excludeCache[node]
        return max(best(root, True), best(root, False))
            



        