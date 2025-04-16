class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        answer = 0
        num2freq = defaultdict(int)
        pairs = 0
        left = 0

        for right in range(len(nums)):
            val = nums[right]
            pairs += num2freq[val]
            num2freq[val] += 1

            while pairs >= k:
                answer += len(nums) - right
                num2freq[nums[left]] -= 1
                pairs -= num2freq[nums[left]]
                left += 1

        return answer

