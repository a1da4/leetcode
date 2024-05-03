class UndergroundSystem:

    def __init__(self):
        self.pathVocab: set(Tuple(str, str)) = set()
        self.path2times: Dict[Tuple(str, str), List[int]] = {}
        self.id2startinfo: Dict[int, Tuple(str, int)] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id2startinfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        _stationName, _t = self.id2startinfo.pop(id)
        if (_stationName, stationName) in self.pathVocab:
            self.path2times[(_stationName, stationName)].append(t - _t)
        else:
            self.path2times[(_stationName, stationName)] = [t - _t]
            self.pathVocab.add((_stationName, stationName))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.path2times[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
