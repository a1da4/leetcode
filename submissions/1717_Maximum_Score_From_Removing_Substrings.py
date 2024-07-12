class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        answer = 0  

        highSubstring = 'ab' if x > y else 'ba'
        lowSubstring = 'ba' if highSubstring == 'ab' else 'ab'
        if x < y:
            x, y = y, x

        def removeSubstring(s, substring):
            stack = []

            for ch in s:
                if ch == substring[1] and stack and stack[-1] == substring[0]:
                    stack.pop()
                else:
                    stack.append(ch)
            
            return ''.join(stack)
        
        sAfterHigh = removeSubstring(s, highSubstring)
        countAfterHigh = (len(s) - len(sAfterHigh)) // 2
        answer += countAfterHigh * x

        sAfterLow = removeSubstring(sAfterHigh, lowSubstring)
        countAfterLow = (len(sAfterHigh) - len(sAfterLow)) // 2
        answer += countAfterLow * y

        return answer

