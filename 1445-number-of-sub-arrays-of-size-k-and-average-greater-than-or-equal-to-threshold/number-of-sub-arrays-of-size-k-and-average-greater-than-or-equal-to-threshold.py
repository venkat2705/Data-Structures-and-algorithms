class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r, ans, running_sum = 0, 0, 0, 0
        if threshold == 0:
            return len(arr)-k+1
        while r < len(arr):
            running_sum += arr[r]
            running_avg = running_sum/k
            if r-l+1 == k:
                if running_avg >= threshold:
                    ans+=1
                running_sum -= arr[l]
                l+=1
            r+=1
        return ans

        