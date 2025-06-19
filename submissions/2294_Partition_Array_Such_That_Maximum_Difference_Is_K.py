class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        answer = 1
        nums.sort()
        currNum = nums[0]
        for num in nums[1:]:
            if num - currNum > k:
                answer += 1
                currNum = num
        return answer
