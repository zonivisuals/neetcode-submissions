class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #more optimal approach
        
        def countKey(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            return count

        res = defaultdict(list)
        for s in strs:
            key = tuple(countKey(s))
            res[key].append(s)

        return list(res.values())