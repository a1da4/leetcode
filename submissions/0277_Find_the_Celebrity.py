# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebs = set(range(n))

        for i in range(n):
            if i not in celebs:
                continue
            for j in range(n):
                if i == j:
                    continue
                i_knows_j = knows(i, j)
                j_knows_i = knows(j, i)
                if i in celebs and (i_knows_j or not j_knows_i):
                    celebs.remove(i)
                if j in celebs and (j_knows_i or not i_knows_j):
                    celebs.remove(j)
                
                if i not in celebs:
                    break

        if celebs:
            return celebs.pop()
        else:
            return -1
