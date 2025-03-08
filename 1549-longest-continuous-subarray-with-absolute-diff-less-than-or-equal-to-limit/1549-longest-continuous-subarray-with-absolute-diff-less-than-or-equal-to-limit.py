class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = 0
        max_ = 0
        st_i = deque()
        st_d = deque()
        for i,n in enumerate(nums):
            while st_i and st_i[-1] < n:
                st_i.pop()
            st_i.append(n)
            while st_d and st_d[-1] > n:
                st_d.pop()
            st_d.append(n)
            while st_i[0] - st_d[0] > k:
                if st_i[0] == nums[l]:
                    st_i.popleft()
                if st_d[0] == nums[l]:
                    st_d.popleft()
                l+=1
            max_ = max(max_, i-l+1)
        return max_


                



                


            



        