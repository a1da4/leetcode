class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N < 3:
            return []

        nums.sort()

        answer = []
        for leftId in range(N - 2):
            if nums[leftId] > 0:
                break
            if leftId != 0 and nums[leftId] == nums[leftId-1]:
                continue

            midId = leftId + 1
            rightId = N - 1
            while (midId < rightId):
                currSum = nums[leftId] + nums[midId] + nums[rightId]
                if (currSum > 0):
                    rightId -= 1
                elif (currSum < 0):
                    midId += 1
                else:
                    answer.append([nums[leftId], nums[midId], nums[rightId]])
                    while (midId < rightId and nums[midId] == nums[midId+1]):
                        midId += 1
                    while (midId < rightId and nums[rightId] == nums[rightId-1]):
                        rightId -= 1
                    midId += 1
                    rightId -= 1

        return answer
