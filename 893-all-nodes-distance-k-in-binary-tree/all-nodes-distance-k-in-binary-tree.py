# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root,par=None):
            if root:
                root.par=par
                dfs(root.left,root)
                dfs(root.right,root)
        dfs(root)
        
        queue = deque([(target,0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node,lev in queue]
            node,lev = queue.popleft()
            for next_level_ele in (node.left, node.right, node.par):
                if next_level_ele and next_level_ele not in seen:
                    seen.add(next_level_ele)
                    queue.append((next_level_ele,lev+1))
        return []
            
            
        
        