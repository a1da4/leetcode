class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        answer = [num for num in nums if num > 0] 
        n_z = n - len(answer)
        if n_z > 0:
            answer += [0] * n_z

        return answer
