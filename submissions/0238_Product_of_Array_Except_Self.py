class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer[0]:         nums[1]*nums[2]*...*nums[-1]
        # answer[1]: nums[0]*        nums[2]*...*nums[-1]
        # answer[2]: nums[0]*nums[1]*        ...*nums[-1]
        numsLength = len(nums)
        answer = [1] * numsLength

        # left side: nums[0]~[i-1]
        currentProduct = 1
        for numsIndex in range(numsLength):
            answer[numsIndex] = currentProduct
            currentProduct *= nums[numsIndex]
        
        # right side: nums[i+1]~nums[-1]
        currentProduct = 1
        for numsIndex in range(numsLength):
            targetIndex = (numsLength - 1) - numsIndex
            answer[targetIndex] *= currentProduct
            currentProduct *= nums[targetIndex]

        return answer
