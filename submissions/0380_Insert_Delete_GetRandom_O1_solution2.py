class RandomizedSet:

    def __init__(self):
        self.data = deque([])
        self.dataDic = {}

    def insert(self, val: int) -> bool:
        if val in self.dataDic:
            return False
        
        self.dataDic[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dataDic:
            return False
        valId = self.dataDic[val]
        self.data[valId], self.data[-1] = self.data[-1], self.data[valId]
        self.dataDic[self.data[valId]] = valId
        self.data.pop()
        self.dataDic.pop(val)
        return True

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
