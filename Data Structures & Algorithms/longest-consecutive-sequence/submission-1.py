class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #eliminated the seq array
        s = set(nums)
        max_seq = 0
        for n in s:
            if (n-1) not in s:
                length = 0
                while(n + length in s):
                    length += 1
                max_seq = max(max_seq, length)
        return max_seq