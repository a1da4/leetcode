class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Initialize list of rows
        listRows = []
        for rowId in range(numRows):
            listRows.append([])
        
        isForward = True
        isBackward = False
        rowIdNow = 0
        for pointer in range(len(s)):
            # append current character
            charNow = s[pointer]
            if isForward:
                listRows[rowIdNow].append(charNow)
                rowIdNow += 1
            if isBackward:
                listRows[rowIdNow].append(charNow)
                rowIdNow -= 1
            
            # update isForward / isBackward
            if rowIdNow < 0:
                isForward = True
                isBackward = False
                rowIdNow += 2
            if rowIdNow >= numRows:
                isForward = False
                isBackward = True
                rowIdNow -= 2
        
        answer = ''.join([''.join(listRow) for listRow in listRows])
        return answer
