# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        current = deque()
        nextLevel = deque()
        current.append(root)
        res = []
        while len(current):
            levelResult = []
            while len(current):
                node = current.popleft()
                levelResult.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(levelResult)
            current = nextLevel
            nextLevel = deque()
        return res
                




        