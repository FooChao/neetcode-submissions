# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = dict()
        for i, v in enumerate(inorder):
            hashMap[v] = i

        def traverse(pl, pr, il, ir):
            if pl > pr:
                return None
            if pl == pr:
                return TreeNode(preorder[pl])
            rootValue = preorder[pl]

            # find the root in inorder
            cur = hashMap[rootValue]
            
            # find size of each side
            leftSize = cur - il
            rightSize = pr - pl + 1 - leftSize - 1

            # build each side
            leftNode = traverse(
                pl + 1, 
                pl + leftSize,
                il,
                il + leftSize - 1
            )

            rightNode = traverse(
                pl + 1 + leftSize,
                pr,
                il + 1 + leftSize,
                ir
            )

            return TreeNode(rootValue, leftNode, rightNode)
        
        return traverse(0, len(preorder) - 1, 0, len(inorder) - 1)
            
            

