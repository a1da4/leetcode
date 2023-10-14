class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if len(nums) == 0:
            return answer

        start = None
        for num in nums:
            if start is None:
                start = num
                series = 0
            else:
                if num == start + series + 1:
                    series += 1
                elif series > 0:
                    answer.append(f"{start}->{start+series}")
                    start = num
                    series = 0
                else:
                    answer.append(str(start))
                    start = num
                    series = 0
        if series > 0:
            answer.append(f"{start}->{start+series}")
        else:
            answer.append(str(start))

        return answer
