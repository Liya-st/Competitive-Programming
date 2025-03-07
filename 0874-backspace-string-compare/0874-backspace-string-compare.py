class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st =[]
        stack = []
        for n in s:
            if n == "#":
                if st:
                    st.pop()
            else:
                st.append(n)
        for n in t:
            if n == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return st == stack

        
        