class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 2**32
        nums1.sort()
        nums2.sort()
        p1,p2 = 0,0
        while p1<len(nums1) and p2<len(nums2):
            print("debug",p1,p2)
            if nums1[p1] == nums2[p2]:
                ans = min(ans,nums1[p1])
                p1+=1
                p2+=1

            elif nums1[p1] < nums2[p2]:
                p1+=1
            else:
                p2+=1

        # for i in nums1:
        #     if i in nums2:
        #         ans = min(ans,i)

        mn1 = min(nums1)
        mn2 = min(nums2)
        return min(mn1,mn2)*10+max(mn1,mn2) if ans == 2**32 else ans
        