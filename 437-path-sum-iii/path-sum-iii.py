# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path_sum_helper(self, root, target):
        if root is None:
            return 0
        res = 0
        if root.val == target:
            res += 1
        res += self.path_sum_helper(root.left, target - root.val)
        res += self.path_sum_helper(root.right, target - root.val)
        return res

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.pathSum(root.left,targetSum) + self.path_sum_helper(root,targetSum) + self.pathSum(root.right,targetSum)

        