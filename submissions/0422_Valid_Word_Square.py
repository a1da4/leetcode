class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        numRow = len(words)
        numCol = max([len(word) for word in words])
        if numRow < numCol:
            return False
        else:
            M = numRow
        mat = [[""] * M for _ in range(M)]

        for kId, word in enumerate(words):
            for currId, char in enumerate(word):
                if mat[kId][currId] == "":
                        mat[kId][currId] = char
                elif mat[kId][currId] == char:
                    pass
                else:
                    return False
                
                if kId != currId:
                    if mat[currId][kId] == "":
                        mat[currId][kId] = char
                    elif mat[currId][kId] == char:
                        pass
                    else:
                        return False

        for kId, word in enumerate(words):
            if ''.join(mat[kId]) == ''.join([mat[i][kId] for i in range(len(mat))]) == word:
                pass
            else:
                return False

        return True

