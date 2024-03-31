class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        leftId = rightId = missId = -1
        for currId, currNum in enumerate(nums):
            if not (minK <= currNum and currNum <= maxK):
                missId = currId
            
            if currNum == minK:
                leftId = currId
            
            if currNum == maxK:
                rightId = currId
            
            answer += max(0, min(leftId, rightId) - missId)

        return answer
