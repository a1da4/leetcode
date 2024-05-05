class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        nums.sort()
        leftNums = nums[:N // 2]
        rightNums = nums[N // 2:]
        _nums = []
        for lNum, rNum in zip(leftNums, rightNums[::-1]):
            _nums.append(lNum)
            _nums.append(rNum)

        if N % 2:
            _nums.append(nums[N // 2])

        nums[:] = _nums

