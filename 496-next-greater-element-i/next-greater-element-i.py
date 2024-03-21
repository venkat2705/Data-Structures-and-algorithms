class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        res = []
        stack = []
        stack.append(nums2[0])
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        for i in stack:
            mapping[i] = -1
        
        for i in nums1:
            res.append(mapping[i])
        return res
                  