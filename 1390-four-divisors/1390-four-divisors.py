class Solution(object):
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for i in nums:
            count = 0
            acc = 0

            for divisor in range(1, int(math.sqrt(i)) + 1):
                if i % divisor == 0:
                    other = i // divisor

                    if divisor == other:
                        count += 1
                        acc += divisor
                    else:
                        count += 2
                        acc += divisor + other

                    if count > 4:
                        break

            if count == 4:
                res += acc

        return res