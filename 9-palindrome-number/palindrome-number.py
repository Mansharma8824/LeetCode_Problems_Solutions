class Solution(object):
    def isPalindrome(self, x):
        Str = str(x)
        return Str == Str[::-1]
        