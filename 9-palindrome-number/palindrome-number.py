class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_rev = x_str[::-1]
        if x_str==x_str_rev:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if x<0:
        #     return False
        # x1 = 0
        # y = x
        # while y:
        #     # print(x,x1)
        #     x1 = x1*10 + y%10
        #     y//=10
        # return x == x1

