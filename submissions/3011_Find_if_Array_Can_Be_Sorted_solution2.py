class Solution:
    def canSortArray(self, nums):
        bits = bin(nums[0]).count("1")
        currMax = nums[0]
        currMin = nums[0]
        prevMin = float("-inf")

        for i in range(1, len(nums)):
            if bin(nums[i]).count("1") == bits:
                currMax = max(currMax, nums[i])
                currMin = min(currMin, nums[i])
            elif currMin < prevMin:
                return False
            else:
                prevMin = currMax
                currMax = nums[i]
                currMin = nums[i]
                bits = bin(nums[i]).count("1")

        return not currMin < prevMin

