# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def mn(root):
            if root == None:
                return 2**32
            res = root.val
            lres = mn(root.left)
            rres = mn(root.right)
            res = min(lres,res,rres)
            return res
        
        def mx(root):
            if root == None:
                return -2**32
            res = root.val
            lres = mx(root.left)
            rres = mx(root.right)
            res = max(lres,res,rres)
            return res
        
        def isbst(root):
            if root == None:
                return True
            if root.left != None and mx(root.left)>=root.val:
                return False
            if root.right != None and mn(root.right)<=root.val:
                return False
            if isbst(root.left) == False or isbst(root.right) == False:
                return False
            return True
        return isbst(root)