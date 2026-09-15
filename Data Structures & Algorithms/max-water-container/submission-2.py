class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ma = 0
        i = 0
        j = len(heights) - 1
        while (i < j):
            width = j - i
            height = min(heights[i],heights[j])
            cw = width*height
            ma = max(ma, cw)
            if (heights[j] > heights[i]):
                i += 1
            else:
                j -= 1
            
                
        return ma

