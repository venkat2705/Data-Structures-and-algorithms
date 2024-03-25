class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def valid(m):
            temp = 0
            for i in ribbons:
                temp += i//m
            return temp
        print(len(ribbons))
        low, high, ans = 1, max(ribbons), 0
        while low <= high:
            mid = (low+high)//2
            if valid(mid) >= k:
                ans = max(ans, mid)
                low = mid + 1
            # elif valid(mid) > k:
            #     low = mid + 1
            else:
                high = mid - 1
        return ans


         
        