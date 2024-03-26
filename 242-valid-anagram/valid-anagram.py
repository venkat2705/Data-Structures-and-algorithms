class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Assign each prime number to the char position ex. a-2, b-3...z-101
        Calculate the product --> as the prime porduct ensures the uniqueness
        if product(s) == product(t) then a anagram
        '''
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
        cnt1, cnt2 = 1, 1
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            cnt1 = cnt1* primes[ord(s[i])-97]
        # for i in range(len(t)):
            cnt2 = cnt2* primes[ord(t[i])-97]
        return cnt1 == cnt2


        