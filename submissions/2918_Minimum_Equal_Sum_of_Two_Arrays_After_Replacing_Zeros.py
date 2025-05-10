class Solution:
    def minSum(
        self, 
        nums1: List[int], 
        nums2: List[int],
    ) -> int:
        nz1, nz2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1), sum(nums2)

        sum1 += nz1
        sum2 += nz2

        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nz1, nz2 = nz2, nz1

        if sum1 != sum2 and nz1 == 0:
            return -1
        
        return sum2
