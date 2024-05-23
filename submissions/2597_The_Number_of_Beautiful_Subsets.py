class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        self.answer = 0

        def search(currId, currNums, currVocab):
            for nextId in range(currId + 1, N):
                nextNum = nums[nextId]
                if currNums == [] or \
                    (nextNum + k not in currVocab \
                        and nextNum - k not in currVocab):
                    self.answer += 1
                    currNums.append(nextNum)
                    currVocab.add(nextNum)
                    search(nextId, currNums, currVocab)
                    is_added = True
                else:
                    is_added = False

                if is_added:
                    currNums.pop()
                    currVocab = set(currNums)

        search(-1, [], set())        

        return self.answer
