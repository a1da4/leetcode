class MyHashMap:

    def __init__(self):
        self.hash = {}
        self.vocab = set()

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value
        self.vocab.add(key)

    def get(self, key: int) -> int:
        if key in self.vocab:
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.vocab:
            self.vocab.remove(key)
            self.hash.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
