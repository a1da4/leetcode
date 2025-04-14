class Solution:
    def countGoodTriplets(
        self, 
        arr: List[int], 
        a: int, 
        b: int, 
        c: int,
    ) -> int:
        answer = 0
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, N):
                    if (abs(arr[j] - arr[k]) <= b
                        and abs(arr[k] - arr[i]) <= c):
                        answer += 1
        
        return answer
