class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minNum = nums[0]
        answer = 0
        for num in nums[1:]:
            if minNum > num:
                minNum = num
            else:
                answer = max(answer, num - minNum) 

        return answer if answer > 0 else -1
