class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp={}
        start=0
        longest=0
        for i in range(len(s)):
            if s[i]  in temp and temp[s[i]]>=start:
                start=temp[s[i]]+1
            temp[s[i]]=i
            longest=max(longest,i-start+1)

        return longest
            


        
