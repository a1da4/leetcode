class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        leftId = 0
        rightId = len(height) - 1

        while leftId < rightId:
            currentArea = (rightId - leftId) * min(height[leftId], height[rightId])
            area = max(area, currentArea)
            if height[leftId] < height[rightId]:
                leftId += 1
            else:
                rightId -= 1

        return area
