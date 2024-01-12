class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed1 = [0]
        flowerbed1.extend(flowerbed)
        flowerbed1.append(0)
        print(flowerbed1)
        p1, p2,l = 0,2,len(flowerbed1)
        cnt=0
        # if l==1 and flowerbed[0] == 0:
        #     return True
        # if (l >= 2):
        #     if (flowerbed[0] == 0 and flowerbed[1] == 0):
        #         cnt+=1
        #     if l>2 and (flowerbed[l-1] == 0 and flowerbed[l-2] == 0):
        #         cnt+=1

        while p2<l:
            if flowerbed1[p1]!=1 and flowerbed1[p2]!=1 and flowerbed1[p1+1]!=1:
                cnt+=1
                flowerbed1[p1+1] = 1
            p1+=1
            p2+=1
        return cnt>=n
        