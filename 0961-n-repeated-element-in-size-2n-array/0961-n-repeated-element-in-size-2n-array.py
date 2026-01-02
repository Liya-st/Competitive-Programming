class Solution(object):
    def repeatedNTimes(self, A):
        count = Counter(A)
        for i in count:
            if count[i] == len(A) // 2:
                return i