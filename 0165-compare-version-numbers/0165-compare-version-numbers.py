class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        c1 = list(map(int, version1.split(".")))
        c2 = list(map(int, version2.split(".")))

        length = max(len(c1), len(c2))
        for i in range(length):
            temp1 = c1[i] if i < len(c1) else 0
            temp2 = c2[i] if i < len(c2) else 0
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1
        return 0


        