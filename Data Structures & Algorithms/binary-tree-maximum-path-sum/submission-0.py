# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax = -float('inf')

        def helper(node: Optional[TreeNode]) -> int:
            """
                Update the global variables and 
                return the best path including the node and one or no side
            """
            nonlocal globalMax
            if node == None:
                return 0
            l, r = helper(node.left), helper(node.right)
            globalMax = max(globalMax,
                node.val,
                node.val + l,
                node.val + r,
                node.val + l + r
            )
            return max(node.val, node.val +l, node.val + r)

        helper(root)
        return globalMax       
        