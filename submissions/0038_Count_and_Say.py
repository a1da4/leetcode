class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        prevRLE = self.countAndSay(n - 1)
        answer = ''
        stack = deque([])
        for digit in prevRLE:
            if stack and stack[-1] == digit:
                pass
            else:
                count = 0
                while stack:
                    num = stack.pop()
                    count += 1
                if count > 0:
                    answer += str(count) + num
            
            stack.append(digit)
        
        if stack:
            count = 0
            while stack:
                num = stack.pop()
                count += 1
            answer += str(count) + num

        return answer

