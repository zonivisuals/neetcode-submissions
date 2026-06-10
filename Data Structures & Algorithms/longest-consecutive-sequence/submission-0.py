class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_seq = 0
        for n in s:
            seq = []
            if (n-1) not in s:
                seq.append(n)
                k = n + 1
                while(k in s):
                    seq.append(k)
                    k+=1
                max_seq = max(max_seq, len(seq))
        return max_seq