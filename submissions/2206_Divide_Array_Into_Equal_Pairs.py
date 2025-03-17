class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for num, freq in Counter(nums).items():
            if freq % 2:
                return False
        
        return True
