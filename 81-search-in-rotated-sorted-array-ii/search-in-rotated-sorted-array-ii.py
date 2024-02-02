class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return True
            elif nums[m] > nums[l]:
                if target < nums[m] and target >= nums[l]:
                    h = m - 1
                else:
                    l = m + 1 
            elif nums[m] < nums[l] :
                if target <= nums[h] and target > nums[m]:
                    l = m+1
                else:
                    h = m-1
            else:
                l+=1
        return False
        