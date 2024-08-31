class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = 0
        self.memory = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.memory[index].append([self.snapId, val])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.memory[index], 
                                        [snap_id, 10 ** 9])
        return self.memory[index][snap_index - 1][1]

