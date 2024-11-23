class Solution:
    def _searchMaxForm(self,
                       dicts: Dict[Tuple[int, int, int], int],
                       currId: int,
                       numZero: int,
                       numOne: int) -> int:
        
        if currId >= len(dicts):
            return 0
        if (currId, numZero, numOne) not in self.memo:
            currDict = dicts[currId]
            if numZero - currDict["0"] >= 0 and numOne - currDict["1"] >= 0:
                num = 1 + self._searchMaxForm(dicts, currId + 1,
                                              numZero - currDict["0"],
                                              numOne - currDict["1"])
            else:
                num = 0
            _num = self._searchMaxForm(dicts, currId + 1, numZero, numOne)
                
            self.memo[(currId, numZero, numOne)] = max(num, _num)
        
        return self.memo[(currId, numZero, numOne)]


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.memo: Dict[Tuple[int, int, int], int] = {}
        dicts: List[Dict[str, int]] = []
        for s in strs:
            d = {}
            d["0"] = s.count("0")
            d["1"] = len(s) - d["0"]
            dicts.append(d)

        return self._searchMaxForm(dicts, 0, m, n)

