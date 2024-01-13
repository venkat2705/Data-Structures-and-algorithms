class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 2**32
        for i in nums1:
            if i in nums2:
                ans = min(ans,i)

        mn1 = min(nums1)
        mn2 = min(nums2)
        return min(mn1,mn2)*10+max(mn1,mn2) if ans == 2**32 else ans
        