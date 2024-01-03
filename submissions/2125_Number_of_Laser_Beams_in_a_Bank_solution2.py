class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        currDevs = []
        for row in bank:
            devices = row.count("1")
            if devices > 0:
                currDevs.append(devices)
        if len(currDevs) > 1:
            return sum([dev0 * dev1 for dev0, dev1 in zip(currDevs[:-1], currDevs[1:])])
        else:
            return 0
