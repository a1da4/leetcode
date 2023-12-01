class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        
        nums1 = nums1 + nums2
        nums1.sort()
        num = nums1[n//2]
        if n%2:
            return num
        else:
            return (num + nums1[n//2-1]) / 2
