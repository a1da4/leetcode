class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        zeroIds = [_id for _id in range(N) if nums[_id] == 0]

        if len(zeroIds) <= 1:
            return N
        else:
            maxOnes = max(zeroIds[1], N - zeroIds[-2] - 1)
            for midId in range(1, len(zeroIds) - 1):
               leftZeroId = zeroIds[midId - 1]
               rightZeroId = zeroIds[midId + 1]
               currOnes = rightZeroId - leftZeroId - 1
               maxOnes = max(maxOnes, currOnes)

            return maxOnes
