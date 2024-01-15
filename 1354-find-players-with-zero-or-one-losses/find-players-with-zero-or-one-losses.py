class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose, win = {}, {}
        ans=[]
        for i in matches:
            # print("debug")
            if i[1] not in lose:
                lose[i[1]] = 1
            else:
                lose[i[1]] += 1
            
            if i[0] not in win:
                win[i[0]] = 1
            else:
                win[i[0]] += 1
        temp1, temp2 = [], []
        for key in win:
            if key not in lose:
                temp1.append(key)
        for key in lose:
            if lose[key] == 1:
                temp2.append(key)
        temp1.sort()
        temp2.sort()
        ans.append(temp1)
        ans.append(temp2)
        return ans


        print(lose,win)

        
        