class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # set vocab.
        numVocab = {'0', '1', '2', '3', '4', 
                    '5', '6', '7', '8', '9'}
        pnVocab = {'+', '-'}
        
        numExist = False
        answer = ''
        for sEach in s:
            # leading spaces are read and ignored
            if sEach == ' ':
                if len(answer) == 0:
                    continue
                else:
                    break
            
            if sEach in numVocab:
                answer += sEach
                numExist = True
            elif sEach in pnVocab:
                # + or - must appear at the beginning
                if len(answer) == 0:
                    answer += sEach
                else:
                    break
            elif sEach == '.':
                # output is expected integer, not float
                break
            else:
                # characters are ignored
                if len(answer) == 0:
                    return 0
                break
        
        if numExist:
            answer = int(answer)
            
            # 32-bit signed integer range
            if answer < -2**31:
                answer = -2**31
            if answer > 2**31 - 1:
                answer = 2**31 - 1

            return answer
        else:
            # there are no digits -> 0
            return 0
