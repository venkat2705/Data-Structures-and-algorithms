class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1 = s[0:n//2]
        s2 = s[n//2:]
        s1_c,s1_v,s2_c,s2_v = 0,0,0,0
        for i in range(n//2):
            if s1[i] in vowels:
                s1_v+=1
            else:
                s1_c+=1
            if s2[i] in vowels:
                s2_v+=1
            else:
                s2_c+=1
        return s1_c == s2_c and s1_v == s2_v
        