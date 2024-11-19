class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        currSum = 0
        begin = 0
        end = 0
        num2id = {}

        while end < len(nums):
            num = nums[end]
            occur = num2id.get(num, -1)
            while begin <= occur or end - begin + 1 > k:
                currSum -= nums[begin]
                begin += 1
            currSum += nums[end]
            num2id[num] = end
            if end - begin + 1 == k:
                answer = max(answer, currSum)
            end += 1

        return answer

