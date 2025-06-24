class Solution:
    def findKDistantIndices(
        self, 
        nums: List[int], 
        key: int, 
        k: int,
    ) -> List[int]:
        answer = []

        N = len(nums)
        windowId = 0

        for currId, num in enumerate(nums):
            if nums[currId] == key:
                if windowId < currId - k:
                    windowId = currId - k
                while windowId <= currId + k and windowId < N:
                    answer.append(windowId)
                    windowId += 1

        return answer
