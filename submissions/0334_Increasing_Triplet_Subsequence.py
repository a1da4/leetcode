class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = float("inf")
        secondNum = float("inf")

        for currentNum in nums:
            if currentNum <= firstNum:
                firstNum = currentNum
            elif currentNum <= secondNum:
                secondNum = currentNum
            else:
                return True

        return False
