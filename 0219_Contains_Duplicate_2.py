class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num2id = {}

        for id, num in enumerate(nums):
            if num in num2id and abs(num2id[num] - id) <= k:
                return True
            else:
                num2id[num] = id
        
        return False
