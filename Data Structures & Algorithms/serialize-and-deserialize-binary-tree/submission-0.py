# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        res = ""
        def helper(node: Optional[TreeNode]) -> None:
            nonlocal serial
            if node == None:
                serial.append("N,")
            else:
                serial.append(str(node.val) + ",")
                helper(node.left)
                helper(node.right)

        helper(root)
        print(serial)
        res = res.join(serial)
        print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        parts = data.split(",")
        parts.pop()
        current = 0
        def helper() -> Optional[TreeNode]:
            nonlocal current
            print(parts, current)
            value = parts[current]
            current += 1
            if value == "N":
                return None
            else:
                res = TreeNode(int(value))
                res.left = helper()
                res.right = helper()
                return res
        return helper()




        
