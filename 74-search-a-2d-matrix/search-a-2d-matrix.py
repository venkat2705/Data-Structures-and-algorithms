class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force will be search entire matrix - T.C - O(m*n)
        # target > 1st and target < last
        # [1,3,5,7] target = 3 - O(mlogn)
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1
        while low <= high:
            mid = (low+high)//2
            row = mid//n
            col = mid%n
            if matrix[row][col] > target:
                high = mid-1
            elif matrix[row][col] < target:
                low = mid+1
            else:
                return True
        return False

        