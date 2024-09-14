class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            isEven = (r - m) % 2 == 0
            if nums[m] == nums[m + 1]:
                if isEven:
                    l = m + 2
                else:
                    r = m - 1

            elif nums[m - 1] == nums[m]:
                if isEven:
                    r = m - 2
                else:
                    l = m + 1

            else:
                return nums[m]

        return nums[l]

