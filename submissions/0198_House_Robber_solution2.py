class Solution:
    def rob(self, nums: List[int]) -> int:
        wRob = woRob = 0
        for num in nums:
            wRobNew = woRob + num
            woRobNew = max(woRob, wRob)
            wRob, woRob = wRobNew, woRobNew              
            
        return max(wRob, woRob)
