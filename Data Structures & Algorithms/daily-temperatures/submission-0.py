class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ansStack = [0] * len(temperatures)
        i = len(temperatures) -1
        
        stack = []
        
        while i >= 0:
            curTemp = temperatures[i]
            
            while stack and temperatures[stack[-1]] <= curTemp:
                stack.pop()

            if stack:
                ansStack[i] = stack[-1] - i
            else:
                ansStack[i] = 0

            stack.append(i)
            i -= 1
        return ansStack
