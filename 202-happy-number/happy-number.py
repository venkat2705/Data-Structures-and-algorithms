class Solution:
    def isHappy(self, n: int) -> bool:
        # if n == 1:
        #     return True
        while True:
            r = 0
            res = 0
            while n:
                r = n%10
                res += r*r
                n //= 10
            if res == 1:
                return True
            if res < 7:
                return False
            n = res


            



        