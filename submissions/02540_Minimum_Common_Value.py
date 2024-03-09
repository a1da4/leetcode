class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = list(set(nums1)&set(nums2))
        if nums3:
            return sorted(nums3)[0]
        else:
            return -1
