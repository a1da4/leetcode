class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        for region1, region2 in zip(version1, version2):
            if int(region1) > int(region2):
                return 1
            if int(region1) < int(region2):
                return -1
        
        if len(version1) > len(version2):
            for region1 in version1[len(version2):]:
                if int(region1) > 0:
                    return 1

        if len(version1) < len(version2):
            for region2 in version2[len(version1):]:
                if int(region2) > 0:
                    return -1

        return 0
    
