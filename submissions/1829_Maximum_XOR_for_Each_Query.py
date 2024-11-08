class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = 2 ** maximumBit - 1
        answer = []
        curr = nums[0]
        for num in nums[1:]:
            curr ^= num

        for num in nums[::-1]:
            answer.append(curr ^ target)
            curr ^= num

        return answer

