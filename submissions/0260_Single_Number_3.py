class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        currId = 0
        while currId < len(nums):
            if currId == len(nums) - 1:
                answer.append(nums[currId])
            elif nums[currId] == nums[currId + 1]:
                currId += 1
            else:
                answer.append(nums[currId])
            currId += 1

        return answer

