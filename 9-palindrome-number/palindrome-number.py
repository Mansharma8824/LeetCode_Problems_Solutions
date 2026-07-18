class Solution(object):
    def isPalindrome(self, x):
        pal = 0
        original = x
        while x > 0:
            rem = x%10
            pal = pal*10 + rem
            x= x//10
        if pal == original:
            return True
        else:
            return False

        