class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        curr = k % sum(chalk)
        if curr > 0:
            for student, _chalk in enumerate(chalk):
                if curr < _chalk:
                    return student
                
                curr -= _chalk
    
        return 0

