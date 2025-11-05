class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        if n == 1:
            return prev

        for _ in range(2, n + 1):
            temp = []
            p = prev[0]
            c = 1
            for i in range(1, len(prev)):
                if prev[i] == p:
                    c +=1
                    continue
                else:
                    temp.append(str(c))
                    temp.append(p)
                    p = prev[i]
                    c = 1
            temp.append(str(c))
            temp.append(p)
            prev = "".join(temp)
        return prev

        