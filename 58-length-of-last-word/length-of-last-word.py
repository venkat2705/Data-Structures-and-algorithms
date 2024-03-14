class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=list(map(str,s.split(" ")))
        s_list = s.split(' ')
        print(arr)
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i]) > 0:
                return len(arr[i])
        
        