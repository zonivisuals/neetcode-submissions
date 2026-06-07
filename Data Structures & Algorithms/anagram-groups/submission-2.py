class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def validAnagram(s, t):
            if len(s) != len(t): return False
            ds = {}
            for c in s:
                if c not in ds:
                    ds[c] = 1
                else:
                    ds[c] = ds[c] + 1
            for c in t:
                if c not in ds:
                    return False
                ds[c] -= 1
            for k,v in ds.items():
                if v != 0 : return False
            return True
            
        
        ga = {}
        for s in strs:
            placed = False
            for key in ga:
                if validAnagram(key, s):
                    ga[key].append(s)
                    placed = True
                    break
            if not placed:
                ga[s] = [s]

        res = []
        for key,value in ga.items():
            res.append(value)
        return res 