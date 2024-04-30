class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reverse_x = x_str[::-1]

        if x_str == reverse_x:
            return True
        else:
            return False