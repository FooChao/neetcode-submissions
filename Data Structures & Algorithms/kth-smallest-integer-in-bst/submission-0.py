# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.helper(root, k)[0].val
    
    #  take in position needed and return needed node if found and size
    def helper(self, node: Optional[TreeNode], position) -> Tuple(Optional[TreeNNode], int):
        if node == None:
            return (None, 0)
        
        # find size of left size and node if found
        nodeFound, leftSize = self.helper(node.left, position)

        if nodeFound:
            return nodeFound, float('inf')
        
        if leftSize + 1 == position:
            return node, float('inf')
        
        nodeFound, rightSize = self.helper(node.right, position - leftSize - 1)
        return nodeFound, leftSize + rightSize + 1

        


        