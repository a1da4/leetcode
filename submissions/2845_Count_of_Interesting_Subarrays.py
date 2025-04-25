class Solution:
    def countInterestingSubarrays(
        self, 
        nums: List[int], 
        modulo: int, 
        k: int
    ) -> int:
        flags = [1 if num % modulo == k else 0 for num in nums]
        
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        answer = 0
        
        for f in flags:
            prefix = (prefix + f) % modulo
            need = (prefix - k) % modulo
            answer += count[need]
            count[prefix] += 1
        
        return answer

