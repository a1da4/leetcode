class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        curr = 0

        while k > 0:
            curr += 1
            if curr not in arr_set:
                k -= 1
        
        return curr
