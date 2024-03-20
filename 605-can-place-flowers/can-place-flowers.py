class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed_temp = [0]
        flowerbed_temp.extend(flowerbed)
        flowerbed_temp.append(0)
        p1, p2, l, ans = 0, 2, len(flowerbed_temp), 0
        while p2 < l:
            if flowerbed_temp[p1] != 1 and flowerbed_temp[p1+1] != 1 and flowerbed_temp[p2] != 1:
                ans += 1
                flowerbed_temp[p1+1] = 1
            p1 += 1
            p2 += 1
        return ans >= n
        
        
        
        
        
        
        
        
        
        
        
        
        
        # flowerbed1 = [0]
        # flowerbed1.extend(flowerbed)
        # flowerbed1.append(0)
        # p1, p2,l = 0,2,len(flowerbed1)
        # cnt=0
        # while p2<l:
        #     if flowerbed1[p1]!=1 and flowerbed1[p2]!=1 and flowerbed1[p1+1]!=1:
        #         cnt+=1
        #         flowerbed1[p1+1] = 1
        #     p1+=1
        #     p2+=1
        # return cnt>=n
        