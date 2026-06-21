class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #revisualize the pattern
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            cv = temperatures[i]
            while(stack and temperatures[stack[-1]] < cv):
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
        return res