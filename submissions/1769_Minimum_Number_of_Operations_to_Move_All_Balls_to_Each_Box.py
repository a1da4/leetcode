class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        N = len(boxes)
        for currId in range(N):
            curr = 0
            if currId > 0:
                for left in range(currId):
                    if boxes[left] == "1":
                        curr += currId - left
            
            if currId != N - 1:
                for right in range(N - 1, currId, -1):
                    if boxes[right] == "1":
                        curr += right - currId
            
            answer.append(curr)

        return answer

