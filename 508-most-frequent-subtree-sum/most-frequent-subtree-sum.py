# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()
        def dfs(root):
            if not root:
                return 0
            s = root.val + dfs(root.left) + dfs(root.right)
            freq[s] += 1
            return s
        dfs(root)
        mx_freq = max(freq.values())
        ans = []
        for k,v in freq.items():
            if v == mx_freq:
                ans.append(k) 
        return ans


        