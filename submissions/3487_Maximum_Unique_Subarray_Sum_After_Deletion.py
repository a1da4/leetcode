class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = 0  
        vocab = set()
        if max(nums) < 0:
            return max(nums)

        for num in nums:
            if num in vocab or num < 0:
                continue
            else:
                answer += num
                vocab.add(num)

        return answer

