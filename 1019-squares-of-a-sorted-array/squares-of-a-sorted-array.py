class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        l, r, ret = 0, len(A) - 1, len(A) - 1
        l_sq, r_sq = A[l] ** 2, A[r] ** 2
        while l <= r:
            if l_sq > r_sq:
                ans[ret] = l_sq
                l += 1
                l_sq = A[l]**2
            else:
                ans[ret] = r_sq
                r -= 1
                r_sq = A[r]**2
            ret-=1
        return ans

