class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        curr = arr[0]
        xors = [curr]
        for num in arr[1:]:
            curr ^= num
            xors.append(curr)

        answer = []
        for [start, end] in queries:
            if start == 0:
                answer.append(xors[end])
            elif start < end:
                answer.append(xors[start - 1] ^ xors[end]) 
            else:
                answer.append(arr[start])

        return answer

