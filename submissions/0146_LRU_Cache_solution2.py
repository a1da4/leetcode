class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.key2val:
            value = self.key2val[key]
            self.key2val.move_to_end(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.key2val.move_to_end(key)
            self.key2val[key] = value
        else:
            self.key2val[key] = value
            if len(self.key2val) > self.capacity:
                self.key2val.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
