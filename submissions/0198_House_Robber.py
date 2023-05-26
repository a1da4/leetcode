class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMoney = 0
        currentMoney = 0
        for num in nums:
            tempMoney = prevMoney
            prevMoney = currentMoney
            currentMoney = max(num + tempMoney, prevMoney)

        return currentMoney
