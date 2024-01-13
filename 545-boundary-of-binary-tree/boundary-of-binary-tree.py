# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        boundaries = [root.val]
        def left(root):
            if not root:
                return
            if root.left or root.right :
                boundaries.append(root.val)
            if root.left:
                left(root.left)
            elif root.right:
                left(root.right)
        left(root.left)

        def leaves(root):
            if not root:
                return
            if not root.left and not root.right:
                boundaries.append(root.val)
            else:
                leaves(root.left)
                leaves(root.right)
        if root.left == None and root.right == None:
            return boundaries
        leaves(root)

        def right(root):
            if not root:
                return
            if root.right:
                right(root.right)
            elif root.left:
                right(root.left)
            if root.left or root.right :
                boundaries.append(root.val)
        right(root.right)
        return boundaries
