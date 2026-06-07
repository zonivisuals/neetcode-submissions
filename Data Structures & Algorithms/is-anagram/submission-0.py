class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sd[s[i]] = (sd[s[i]] + 1) if s[i] in sd else 1
            td[t[i]] = (td[t[i]] + 1) if t[i] in td else 1
        
        for k,v in sd.items():
            if k not in td or td[k] != v:
                return False
        return True