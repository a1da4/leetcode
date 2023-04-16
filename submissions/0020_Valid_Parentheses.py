class Solution:
    def isValid(self, s: str) -> bool:
        # quere / pop based method
        leftParens = []

        leftVocab = {'(', '[', '{'}
        rightVocab = {')', ']', '}'}
        pairParens = {'(': ')', '[': ']', '{': '}'}

        for sCurrent in s:
            if sCurrent in leftVocab:
                leftParens.append(sCurrent)
            elif sCurrent in rightVocab:
                # leftParen does not exist -> False
                if len(leftParens) == 0:
                    return False
                # {[]} -> True, ([)] -> False
                if pairParens[leftParens[-1]] == sCurrent:
                    leftParens.pop(-1)
                else:
                    return False
            else:
                continue
        
        return len(leftParens) == 0
