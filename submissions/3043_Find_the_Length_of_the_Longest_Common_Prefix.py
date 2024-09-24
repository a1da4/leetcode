class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        v1 = set()
        for val in arr1:
            while val not in v1 and val > 0:
                v1.add(val)
                val //= 10
        
        answer = 0
        for val in arr2:
            while val not in v1 and val > 0:
                val //= 10
            
            if val > 0:
                answer = max(answer, len(str(val)))

        return answer

