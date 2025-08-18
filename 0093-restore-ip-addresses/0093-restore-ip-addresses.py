class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) < 4 or len(s) > 12:
            return []
        def check(s):
            if len(s) > 3 or not s:
                return False
            if len(s) > 1 and s[0] == "0":
                return False
            return 0 <= int(s) <= 255

        def backtrack(idx, segments, res):
            if idx == len(s) and len(segments) == 4:
                res.append(".".join(segments))
                return
            if idx >= len(s) or len(segments) == 4:
                return

            for i in range(1, 4):
                if idx + i > len(s):
                    continue
                temp = s[idx: idx+i]
                if check(temp):
                    segments.append(temp)
                    backtrack(idx+i, segments, res)
                    segments.pop()
        backtrack(0, [], res)
        return res
