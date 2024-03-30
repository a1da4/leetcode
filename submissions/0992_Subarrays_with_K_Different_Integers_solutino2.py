class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        num2freq = Counter()
        answer = curr = 0
        leftId = 0

        for rightId, num in enumerate(nums):
            num2freq[num] += 1

            if num2freq[num] == 1:
                k -= 1

            if k < 0:
                num2freq[nums[leftId]] -= 1
                if num2freq[nums[leftId]] == 0:
                    k += 1
                leftId += 1
                curr = 0

            if k == 0:
                while num2freq[nums[leftId]] > 1:
                    num2freq[nums[leftId]] -= 1
                    leftId += 1
                    curr += 1
                answer += (curr + 1)

        return answer
