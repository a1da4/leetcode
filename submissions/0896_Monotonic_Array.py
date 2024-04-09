class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = None
        for num_i, num_j in zip(nums[:-1], nums[1:]):
            if num_i == num_j:
                continue
            if is_inc is None:
                is_inc = (num_i < num_j)
            else:
                if is_inc != (num_i < num_j):
                    return False
        return True
