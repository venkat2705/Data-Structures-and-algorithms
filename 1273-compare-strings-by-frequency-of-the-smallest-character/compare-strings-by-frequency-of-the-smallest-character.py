class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_count,query_count = {},{}
        for word in words:
            word_l = sorted(word)
            word_count[word] = word_l.count(word_l[0])
        # print(word_count)
        for query in queries:
            query_l = sorted(query)
            query_count[query] = query_l.count(query_l[0])
        # print(query_count)
        res = []
        for query in queries:
            ans = 0
            for word in words:
                if query_count[query] < word_count[word]:
                    ans+=1
            res.append(ans)
        return res
        


        