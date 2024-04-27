class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def prime_cnt(word):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
            cnt = 1
            for i in word:
                cnt = cnt * primes[ord(i) - ord('a')]
            return cnt
        d={}
        for word in strs:
            word_cnt = prime_cnt(word)
            if word_cnt in d:
                d[word_cnt].append(word)
            else:
                d[word_cnt] = [word]
        return [i for i in d.values()]


            



        #time complexity ==> (N*26+no.of elements present in the dictionary worst case(N))
        