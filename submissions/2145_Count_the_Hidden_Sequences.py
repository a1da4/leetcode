class Solution:
    def numberOfArrays(
        self, 
        differences: List[int], 
        lower: int, 
        upper: int,
    ) -> int:
        n = len(differences)
        diff_i = differences[0]
        min_diff, max_diff = diff_i, diff_i
        for i in range(1, n):
            diff_i += differences[i]
            min_diff = min(min_diff, diff_i)
            max_diff = max(max_diff, diff_i)
        
        answer = 0
        for h_0 in range(lower, upper + 1):
            if self.verify(min_diff, h_0, lower, upper) \
            and self.verify(max_diff, h_0, lower, upper):
                answer += 1

        return answer

    def verify(
        self,
        diff: int,
        hidden: int,
        lower: int,
        upper: int,
    ):
        return lower - hidden <= diff <= upper - hidden

