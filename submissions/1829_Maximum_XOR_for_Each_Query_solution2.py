class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = 2 ** maximumBit - 1
        
        curr = nums[0]
        answer = [curr ^ target]
        for num in nums[1:]:
            curr ^= num
            answer.append(curr ^ target)

        return answer[::-1]

