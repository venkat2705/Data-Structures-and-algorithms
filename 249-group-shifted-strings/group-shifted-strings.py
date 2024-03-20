class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for word in strings:
            key = ()
            for i in range(len(word)-1):
                circular_diff = 26 + ord(word[i]) - ord(word[i+1])
                key += (circular_diff%26,)
            if key in d:
                d[key] += [word]
            else:
                d[key] = []+[word]
        print(d)
        return d.values()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d={}
        # for word in strings:
        #     key = ()
        #     for i in range(len(word)-1):
        #         circular_diff = 26 + ord(word[i+1]) - ord(word[i])
        #         key += (circular_diff%26,)
        #     if key in d:
        #         d[key] += [word]
        #     else:
        #         d[key] = []+[word]
        #     # d[key] = d.get(key,[])+[word]
        # print(d)
        # return list(d.values())