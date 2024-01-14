class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        temp = s[::-1]
        for i in range(len(s)):
            if temp[i] != s[i]:
                ind = i
                break
        temp = temp[:i] + temp[i+1:]
        if temp == temp[::-1]:
            return True
        
        temp = s[:i] + s[i+1:]
        if temp == temp[::-1]:
            return True
        return False
            

        
