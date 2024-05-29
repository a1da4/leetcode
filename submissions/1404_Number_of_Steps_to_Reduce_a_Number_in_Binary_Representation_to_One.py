class Solution:
    def numSteps(self, s: str) -> int:
        answer = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                _s = []
                is_rise = '1'
                for digit in s[::-1]:
                    if is_rise == digit:
                        _s.append('0')
                        is_rise = digit
                    else:
                        if is_rise == '1' or digit == '1':
                            _s.append('1')
                        else:
                            _s.append('0')
                        is_rise = '0'
                s = ''.join(_s[::-1])
                if s[0] == '0':
                    s = '1' + s
            answer += 1
        return answer
