class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = {"val": [], "time": []}
        self.dic[key]["val"].append(value)
        self.dic[key]["time"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # use binary search here
        if key not in self.dic:
            return ""

        vals = self.dic[key]["val"]
        times = self.dic[key]["time"]

        left, right = 0, len(vals)

        while left < right:
            mid = (left + right) // 2
            if times[mid] > timestamp:
                right = mid 
            else:
                left = mid + 1

        if right == 0:
            return ""
        return vals[right - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
