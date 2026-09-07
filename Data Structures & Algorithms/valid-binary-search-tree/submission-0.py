# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, high, low):
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            return (
                helper(node.left, node.val, low) and 
                helper(node.right,high, node.val)
            )
        return helper(root, float('inf'), -float('inf'))
        