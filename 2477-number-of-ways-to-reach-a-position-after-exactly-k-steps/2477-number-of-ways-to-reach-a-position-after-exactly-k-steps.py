class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
       
        MOD=1e9+7
        
        memo={}
        
        def dp(pos ,k):
            if (pos ,k) in memo:
                return memo[(pos ,k)]
				
            if pos == endPos and k==0:
                return 1
            if k <=0:
                return 0
            
            
            left ,right = 0,0

            left +=dp(pos-1 ,k-1)
            right +=dp(pos +1 ,k-1)

            memo[(pos ,k)]=(left +right )%MOD
            return memo[(pos ,k)]
        
        return int(dp(startPos,k)%MOD)
