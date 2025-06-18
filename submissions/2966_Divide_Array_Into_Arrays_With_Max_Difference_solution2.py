class Solution:
    def divideArray(
        self, 
        nums: List[int], 
        k: int,
    ) -> List[List[int]]:
        nums.sort()
        n = len(nums) // 3
        answer = []
        for i in range(n):
            head = i * 3
            if nums[head + 2] - nums[head] > k:
                return []
            answer.append([nums[head], nums[head + 1], nums[head + 2]])
        return answer
