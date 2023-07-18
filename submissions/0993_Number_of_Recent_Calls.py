class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        latestItem = t
        while latestItem - self.queue[0] > 3000:
            self.queue.pop(0)
        
        return len(self.queue)

