class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        def verify(subarr: List[int]) -> bool:
            if len(subarr) == 1:
                return True
            for prev, curr in zip(subarr[:-1], subarr[1:]):
                if prev + 1 != curr:
                    return False
            return True

        answer = []
        subarr = nums[:k]
        for i in range(len(nums) - k + 1):
            # verify
            if verify(subarr):
                answer.append(subarr[-1])
            else:
                answer.append(-1)

            if i + k < len(nums):
                # update (pop + add)
                subarr = subarr[1:]
                subarr.append(nums[i + k])
        
        return answer

