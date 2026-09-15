class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for ia in range(len(nums)):
            if ia > 0 and nums[ia] == nums[ia-1]:
                continue
            a = nums[ia]
            t = -a
            i = ia + 1
            j = len(nums)-1
            while(i<j):
                if (nums[i] + nums[j] < t):
                    i += 1
                elif (nums[i]+nums[j]>t):
                    j -= 1
                else:
                    results.append([a, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while(i<j and nums[i]==nums[i-1]): 
                        i += 1
                    while(i<j and nums[j]==nums[j+1]): 
                        j -= 1
        return results
        

