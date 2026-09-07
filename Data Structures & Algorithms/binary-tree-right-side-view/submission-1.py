# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        currentLevel = [root]
        nextLevel = []
        res = []
        while currentLevel:
            res.append(currentLevel[-1].val)
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            currentLevel = nextLevel
            nextLevel = []
        return res

        