class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1]  = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]
        
        # @cache --> Recursive solution
        # def helper(s):
        #     if len(s) == 0:
        #         return True
        #     for word in wordDict:
        #         if s.startswith(word):
        #             if helper(s[len(word):]):
        #                 return True
        #     return False
        # return helper(s)
