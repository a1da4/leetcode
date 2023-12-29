class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)
        if (N1 + N2) % 2:
            med1 = med2 = int((N1 + N2)//2)
        else:
            med2 = int((N1 + N2) // 2)
            med1 = med2 - 1
        
        nums = []
        id1 = 0
        id2 = 0
        while len(nums) < med2 + 1:
            if id1 >= N1:
                nums.append(nums2[id2])
                id2 += 1
            elif id2 >= N2:
                nums.append(nums1[id1])
                id1 += 1
            else:
                num1 = nums1[id1]
                num2 = nums2[id2]
                if num1 < num2:
                    nums.append(num1)
                    id1 += 1
                else:
                    nums.append(num2)
                    id2 += 1
        return (nums[med1] + nums[med2]) / 2
