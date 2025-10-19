class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = set()
        def backtrack(idx, temp):
            if idx == len(s):
                res.add("".join(temp))
                return
            org = s[idx]
            if org.islower():
                temp.append(org.upper())
            else:
                temp.append(org.lower())
 
            backtrack(idx + 1, temp)
            temp.pop()
            temp.append(org)
            backtrack(idx + 1, temp)
            temp.pop()

        backtrack(0, [])
        return list(res)

            

        