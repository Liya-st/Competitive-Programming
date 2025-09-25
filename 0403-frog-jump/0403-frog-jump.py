class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        def dp(idx, k):
            if idx == len(stones)-1:
                return True
            
            state = (idx, k)
            if state not in memo:
                cur, prev, nxt = False, False, False

                i = bisect.bisect_left(stones, stones[idx] + k + 1)
                if i < len(stones) and stones[i] == stones[idx] + k + 1:
                    nxt = dp(i, k+1)
                if k > 1:
                    i = bisect.bisect_left(stones, stones[idx] + k-1)
                    if  i < len(stones) and stones[i] == stones[idx] + k:
                        prev = dp(i, k -1)
                if k > 0:
                    i = bisect.bisect_left(stones, stones[idx] + k)
                    if  i < len(stones) and stones[i] == stones[idx] + k:
                        cur = dp(i, k)
                memo[state] = cur or prev or nxt
            return memo[state]
        return dp(0, 0)

        