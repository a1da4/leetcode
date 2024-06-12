class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _numzero, _numone, _numtwo = 0, 0, 0
        for num in nums:
            if num == 0:
                _numzero += 1
            if num == 1:
                _numone += 1
            if num == 2:
                _numtwo += 1
        
        nums[:] = [0] * _numzero + [1] * _numone + [2] * _numtwo
