class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic = {}
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                s = "".join(map(str, (num[i], num[i+1], num[i+2])))
                dic[int(s)] = s
        # res
        return dic[max(dic)] if dic else ""
        