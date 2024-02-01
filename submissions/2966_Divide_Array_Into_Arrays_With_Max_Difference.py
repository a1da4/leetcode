class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        currId = 0

        answer = []
        for diff in range(N//3):
            if nums[currId + 3 - 1] - nums[currId] > k:
                return []
            answer.append(nums[currId:currId + 3])
            currId += 3
        
        return answer
