class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:
            return 0
        
        answer = 0
        leftId = 1
        rightId = len(height) - 1
        leftMax = height[0]
        rightMax = height[-1]
        
        while leftId <= rightId:
            if height[leftId] > leftMax:
                leftMax = height[leftId]
            if height[rightId] > rightMax:
                rightMax = height[rightId]
            
            if leftMax <= rightMax:
                answer += leftMax - height[leftId]
                leftId += 1
            else:
                answer += rightMax - height[rightId]
                rightId -= 1
                
        return answer
