# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def recursive(node):
            if not node:
                return None
            if not(node.left or node.right):
                res[-1].append(node.val)
                return None
            node.left = recursive(node.left)
            node.right = recursive(node.right)
            return node
        while root:
            res.append([])
            root = recursive(root)
        return res
                
