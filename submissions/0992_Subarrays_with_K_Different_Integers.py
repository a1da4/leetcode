class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        leftId = 0
        rightId = 0
        N = len(nums)
        num2freq = Counter()
        ansIds = set()
        while rightId < N:
            num2freq[nums[rightId]] += 1
            while num2freq and len(num2freq) > k:
                num = nums[leftId]
                num2freq[num] -= 1
                if num2freq[num] <= 0:
                    num2freq.pop(num)
                leftId += 1
            if len(num2freq) == k:
                _num2freq = num2freq.copy()
                _leftId = leftId
                if (leftId, rightId) in ansIds:
                    pass
                ansIds.add((leftId, rightId))
                while _num2freq and len(_num2freq) == k:
                    ansIds.add((_leftId, rightId))
                    num = nums[_leftId]
                    _num2freq[num] -= 1
                    if _num2freq[num] <= 0:
                        _num2freq.pop(num)
                    _leftId += 1
            rightId += 1

        return len(ansIds)
