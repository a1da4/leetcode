class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def _calcDist(worker: List[int], bike: List[int]) -> int:
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        
        minDist = float('inf')
        dist2pairs = defaultdict(list)
        for workerId, worker in enumerate(workers):
            for bikeId, bike in enumerate(bikes):
                dist = _calcDist(bike, worker)
                dist2pairs[dist].append((workerId, bikeId))
                minDist = min(minDist, dist)

        currDist = minDist
        workerStatus = [-1] * len(workers)
        bikeStatus = [False] * len(bikes)
        numPairs = 0

        while numPairs < len(workers):
            for workerId, bikeId in dist2pairs[currDist]:
                if workerStatus[workerId] == -1 and not bikeStatus[bikeId]:
                    workerStatus[workerId] = bikeId
                    bikeStatus[bikeId] = True
                    numPairs += 1
            currDist += 1

        return workerStatus
