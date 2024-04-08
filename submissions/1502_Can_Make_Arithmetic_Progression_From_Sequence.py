class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        for num1, num2 in zip(arr[:-1], arr[1:]):
            curr = num1 - num2
            if diff != curr:
                return False
        
        return True
