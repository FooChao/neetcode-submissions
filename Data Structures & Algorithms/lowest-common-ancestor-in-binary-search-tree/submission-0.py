# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pv = p.val
        qv = q.val
        current = root
        while current != None:
            cv = current.val
            if cv > qv and cv > pv:
                current = current.left
            elif cv < qv and cv < pv:
                current = current.right
            else:
                return current
            
            
        