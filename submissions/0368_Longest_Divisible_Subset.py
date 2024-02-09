class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        maxSize = 1
        maxId = 0

        for rightId in range(1, len(nums)):
            for leftId in range(rightId):
                if nums[rightId] % nums[leftId] == 0:
                    dp[rightId] = max(dp[rightId], dp[leftId] + 1)
                    if dp[rightId] > maxSize:
                        maxSize = dp[rightId]
                        maxId = rightId

        answer = []
        num = nums[maxId]        
        for leftId in range(maxId, -1, -1):
            if num % nums[leftId] == 0 and dp[leftId] == maxSize:
                answer.append(nums[leftId])
                num = nums[leftId]
                maxSize -= 1

        return answer
