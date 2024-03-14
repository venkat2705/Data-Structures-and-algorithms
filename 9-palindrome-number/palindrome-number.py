class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x1 = int(str(x)[::-1])
        return x == x1

