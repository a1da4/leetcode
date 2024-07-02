class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num1 in nums1:
            if num1 in nums2:
                answer.append(num1)
                nums2.remove(num1)
        
        return answer
