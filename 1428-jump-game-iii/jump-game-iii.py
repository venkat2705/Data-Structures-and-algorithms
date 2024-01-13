class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        def dfs(i):
            if i >= len(arr) or i < 0:
                return False
            if arr[i] == 0:
                return True
            if visited[i]:
                return False
            visited[i] = True
            left = dfs(i-arr[i])
            right = dfs(i+arr[i])
            return left or right
        return dfs(start)
        