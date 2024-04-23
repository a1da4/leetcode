class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                pass
            elif bill == 10:
                if register[5] > 0:
                    register[5] -= 1
                else:
                    return False
            else:
                # bill == 20:
                if register[5] > 0 and register[10] > 0:
                    register[5] -= 1
                    register[10] -= 1
                elif register[5] >= 3: 
                    register[5] -= 3
                else:
                    return False

            register[bill] += 1
        
        return True

