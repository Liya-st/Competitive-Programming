class Solution:
    def maxPower(self, stations, r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for x in stations:
            prefix.append(prefix[-1] + x)  

        base = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            base[i] = prefix[R + 1] - prefix[L]  

        def can_make(target: int) -> bool:
            diff = [0] * (n + 1)  
            cur_add = 0          
            used = 0              

            for i in range(n):
                cur_add += diff[i] 
                cur_power = base[i] + cur_add

                if cur_power < target:
                    need = target - cur_power
                    used += need
                    if used > k:  
                        return False

                    cur_add += need
                    pos = min(n - 1, i + r)
                    end = min(n, pos + r + 1) 
                    diff[end] -= need  
            return True  

        left, right = 0, sum(stations) + k
        res = 0

        while left <= right:
            mid = (left + right) // 2
            if can_make(mid): 
                res = mid
                left = mid + 1 
            else:
                right = mid - 1  

        return res