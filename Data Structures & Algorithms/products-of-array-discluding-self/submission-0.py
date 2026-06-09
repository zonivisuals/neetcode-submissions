class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] 
        p1 = 1
        for i in range(len(nums)-1):
            p1 *= nums[i]
            pref.append(p1)
        print(pref)

        p2 = 1
        suf = [1]
        for i in range(len(nums)-1, 0,-1):
            p2 *= nums[i]
            suf.append(p2)
        print(suf)

        res = []
        for i in range(len(nums)):
            prod = pref[i]*suf[len(suf)-1-i]
            res.append(prod)
        
        return res