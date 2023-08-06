# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        currMin = 1
        currMax = n

        currNum = max(n // 2, currMin)
        currStatus = guess(currNum)
        while currStatus != 0:
            print(f"currNum: {currNum}, currStatus: {currStatus}")
            temp = currNum
            if currStatus == -1:
                # currNum is higher than the picked number
                currMax = currNum - 1
            if currStatus == 1:
                # currNUm is lower than the picked number
                currMin = currNum + 1
            currNum = (currMax + currMin) // 2
            currStatus = guess(currNum)
        
        return currNum
