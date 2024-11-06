class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        #bits = [bin(num).count("1") for num in nums]
        N = len(nums)
        vals = nums.copy()
        for i in range(N):
            for j in range(N - i - 1)
                if vals[j] <= vals[j + 1]:
                    continue
                elif bin(vals[j]).count("1") == bin(vals[j + 1]).count("1"):
                    vals[j], vals[j + 1] = vals[j + 1], vals[j]
                else:
                    return False

        return True

