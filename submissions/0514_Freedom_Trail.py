class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R = len(ring)
        K = len(key)
        bestSteps = {}

        def calcStep(currId: int, nextId: int):
            step = abs(currId - nextId)
            return min(step, R - step)
        
        def unlock(ringId: int, keyId: int, step: int):
            if (ringId, keyId) in bestSteps:
                return bestSteps[(ringId, keyId)]

            if keyId == K:
                bestSteps[(ringId, keyId)] = 0
                return 0

            for nextId in range(R):
                if ring[nextId] == key[keyId]:
                    nextStep = calcStep(ringId, nextId) + 1 + \
                                unlock(nextId, keyId + 1, float("inf"))
                    step = min(step, nextStep)
            bestSteps[(ringId, keyId)] = step
            return step

        return unlock(0, 0, float("inf"))

