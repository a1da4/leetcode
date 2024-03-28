class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = 0
        num2freq = {}
        leftId = 0
        rightId = 0
        N = len(nums)
        while rightId < N:
            num = nums[rightId]
            if num in num2freq:
                num2freq[num] += 1
            else:
                num2freq[num] = 1

            while num2freq[num] > k:
                _num = nums[leftId]
                num2freq[_num] -= 1
                leftId += 1
            
            answer = max(answer, rightId - leftId + 1)
            rightId += 1

        return answer

