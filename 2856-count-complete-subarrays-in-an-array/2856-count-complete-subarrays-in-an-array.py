class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = Counter(nums)
        c = len(count)
        res = 0
        for i in range(len(nums)):
            cnt = Counter([nums[i]])
            for j in range(i, len(nums)):
                cnt[nums[j]] +=1
                if len(cnt) == c:
                    res +=1
        return res

            
                
