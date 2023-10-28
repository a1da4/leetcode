class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.vals = []

    def get(self, key: int) -> int:
        if key in self.keys:
            id = self.keys.index(key)
            value = self.vals[id]
            self.keys.pop(id)
            self.vals.pop(id)
            self.keys.append(key)
            self.vals.append(value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            id = self.keys.index(key)
            self.keys.pop(id)
            self.vals.pop(id)
            self.keys.append(key)
            self.vals.append(value)
        else:
            self.keys.append(key)
            self.vals.append(value)
    
        if len(self.keys) > self.capacity:
            self.keys.pop(0)
            self.vals.pop(0)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
