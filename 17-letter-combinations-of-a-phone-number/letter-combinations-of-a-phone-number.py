class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if len(digits) == 0:
            return []
        res = [""]
        for d in digits:
            temp = []
            for l in letters[d]:
                for o in res:
                    temp.append(o+l)
            res = temp
        return res