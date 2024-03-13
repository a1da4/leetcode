class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        answer = 0
        stack = []
        for currId in range(N):
            while stack and heights[stack[-1]] > heights[currId]:
                tall = stack.pop()
                if len(stack) == 0:
                    curr = heights[tall] * currId
                else:
                    curr = heights[tall] * (currId - stack[-1] - 1)
                answer = max(answer, curr)
            stack.append(currId)
        
        while stack:
            tall = stack.pop()
            if len(stack) == 0:
                curr = heights[tall] * N
            else:
                curr =  heights[tall] * (N - stack[-1] - 1)
            answer = max(answer, curr)
        
        return answer
