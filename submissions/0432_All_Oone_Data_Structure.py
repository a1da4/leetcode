class AllOne:

    def __init__(self):
        self.key2val = {}

    def inc(self, key: str) -> None:
        if key not in self.key2val:
            self.key2val[key] = 1
        else:
            self.key2val[key] += 1

    def dec(self, key: str) -> None:
        if key in self.key2val:
            if self.key2val[key] > 1:
                self.key2val[key] -= 1
            else:
                self.key2val.pop(key)

    def getMaxKey(self) -> str:
        mKey, mVal = "", -1
        for key, val in self.key2val.items():
            if mVal < val:
                mKey, mVal = key, val
        
        return mKey

    def getMinKey(self) -> str:
        mKey, mVal = "", 10**9 + 7
        for key, val in self.key2val.items():
            if mVal > val:
                mKey, mVal = key, val
        
        return mKey


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
