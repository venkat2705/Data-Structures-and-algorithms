class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        p1,p2 = 0,n-1
        ans = 0
        while p1 < p2:
            if people[p1]+people[p2]<=limit:
                ans+=1
                p1+=1
                p2-=1
            else:
                ans+=1
                p2-=1
        if p1==p2:
            return ans+1 
        else:
            return ans
            

        