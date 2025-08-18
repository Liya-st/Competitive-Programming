from itertools import permutations
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        op = ["-", "+", "/", "*"]
        def evaluate(nums, ops):
            if len(nums) == 1:
                return {nums[0]}
            
            result = set()
            for i in range(len(nums) - 1):
                for j in range(len(ops)):
                    res = eval(str(nums[i])+  ops[j] +  str(nums[i + 1]) ) if nums[i+1] != 0 else None
                    if res is None:
                        continue
                    temp = nums[:i] + [res] + nums[i + 2:]
                    ans = evaluate(temp, ops[:j] + ops[j + 1:])
                    result |= ans   

            return result
        for perm in permutations(cards):
            nums = list(perm)
            for o1 in op:
                for o2 in op:
                    for o3 in op:
                        res = evaluate(nums, [o1, o2, o3])
                        for n in res:
                            if n == 24 or abs(n - 24) <= 0.001:
                                return True
        return False
                    