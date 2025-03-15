class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(left, right, turn):
            if right - left < 1:
                if turn % 2:
                    return [nums[left], 0]
                return [0, nums[left]]
            p1, p2 = rec(left + 1, right, turn + 1)
            p11, p22 =rec(left, right - 1, turn+1)
            
            
            if turn % 2:
                p1+=nums[left]
                p11+= nums[right]
                if p1 - p2 > p11 - p22:
                    return[p1 , p2]
                else:
                    return [p11, p22]
            else:
                p2+= nums[left]
                p22+= nums[right]
                if p1 - p2 < p11 - p22:
                    return[p1, p2  ]
                else:
                    return [p11, p22 ]
        p1 , p2 = rec(0, len(nums)- 1, 1)
        return p1 >= p2