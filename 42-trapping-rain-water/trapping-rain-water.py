class Solution:
    def trap(self, height: List[int]) -> int:
        # using pre sum for left and right max
        '''
        This problem can be solved without using extra space as well, need to track the left max and right max values along the way update the answer accordingly.

        amount of water can be on top of building --> height - min(maxLeft, maxRight)

        put two pointers on both ends, check if leftmax < rightmax ==> this means we already have some bigger on the other side so we only care about the leftmax value. here --> height - leftmax and increase left pointer

        else: here --> height - leftmax and decrease right pointer
        '''
        n=len(height)
        ans = 0
        l_max,r_max = [0]*n,[0]*n
        l_max[0] = height[0]
        r_max[-1] = height[-1]
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            r_max[i] = max(r_max[i+1],height[i])
        print(l_max,r_max)
        for i in range(n):
            ans+=min(l_max[i],r_max[i])-height[i]
        return ans


















        # n = len(height)
        # left_max,right_max,ans = [0]*n,[0]*n,[0]*n
        # left_max[0],right_max[-1] = height[0],height[-1]
        # for i in range(1,n):
        #     left_max[i] = max(left_max[i-1],height[i-1])
        #     right_max[n-i-1] = max(right_max[n-i],height[n-i])
        # for i in range(n):
        #     ans[i] = min(left_max[i],right_max[i]) - height[i] if min(left_max[i],right_max[i]) > height[i] else 0
        # return sum(ans)