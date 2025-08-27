class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos_stack = []
        neg_stack = []
        for i , n in enumerate(asteroids):
            flag = False

            if n > 0:
                pos_stack.append((i, n))
            else:
                if pos_stack:
                    while pos_stack:
                        if pos_stack[-1][1] > abs(n):
                            flag = False
                            break
                        elif pos_stack[-1][1] < abs(n):
                            pos_stack.pop()
                            flag = True
                        else:
                            pos_stack.pop()
                            flag = False
                            break
                    if flag:
                        neg_stack.append((i, n))
                else:
                    neg_stack.append((i, n))
        pos_stack.extend(neg_stack)
        pos_stack.sort()
        res = [n for i, n in pos_stack]
        return res
