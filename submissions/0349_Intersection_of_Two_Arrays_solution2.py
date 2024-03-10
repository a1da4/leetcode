class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums12 = set()
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                nums12.add(num)
        return list(nums12)
