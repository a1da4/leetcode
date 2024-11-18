class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        revCode = code[::-1]
        N = len(code)
        for currId in range(N):
            if k == 0:
                num = 0
            elif k > 0:
                if currId + k < N:
                    num = sum(code[currId + 1:currId + k + 1])
                else:
                    num = sum(code[currId + 1:]) \
                        + sum(code[:currId + k + 1 - N])
            else:
                if currId + k >= 0:
                    num = sum(code[currId + k:currId])
                else:
                    num = sum(code[:currId]) \
                        + sum(revCode[:abs(k) - currId])
            
            answer.append(num)


        return answer

