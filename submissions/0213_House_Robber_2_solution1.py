class Solution:
    def rob(self, nums: List[int]) -> int:

        def search(nums: List[int]) -> int:
            # answer of House Robber 1
            prevMoney = 0
            currentMoney = 0

            for i in range(len(nums)):
                tempMoney = prevMoney
                prevMoney = currentMoney

                if nums[i] + tempMoney > prevMoney:
                    currentMoney = nums[i] + tempMoney
                else:
                    currentMoney = prevMoney

            return currentMoney
        
        if len(nums) == 1:
            return nums[0]
    
        return max(search(nums[1:]), search(nums[:-1]))
