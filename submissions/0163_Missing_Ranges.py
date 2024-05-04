class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        answer = []
        if len(nums) == 0:
            answer.append([lower, upper])
        elif len(nums) == 1:
            if lower < nums[0]:
                answer.append([lower, nums[0] - 1])
            if nums[0] < upper:
                answer.append([nums[0] + 1, upper])
        elif len(nums) == len(range(lower, upper + 1)):
            pass
        else:
            if lower < nums[0]:
                answer.append([lower, nums[0] - 1])
             
            for num_i, num_j in zip(nums[:-1], nums[1:]):
                if num_i + 1 == num_j:
                    continue

                answer.append([num_i + 1, num_j - 1])

            if nums[-1] < upper:
                answer.append([nums[-1] + 1, upper])

        return answer
