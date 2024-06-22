class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answer = 0
        _answer = 0
        leftId = 0
        curr = 0
        for rightId in range(len(nums)):
            curr += nums[rightId]%2
            if curr == k:
                _answer = 0
                while curr == k:
                    curr -= nums[leftId]%2
                    _answer += 1
                    leftId += 1
            answer += _answer

        return answer

