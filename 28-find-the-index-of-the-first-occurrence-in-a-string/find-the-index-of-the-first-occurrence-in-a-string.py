class Solution(object):
    def strStr(self, haystack, needle):
        slow = 0
        while slow < len(haystack):
            if haystack[slow:slow+len(needle)] == needle:
                return slow
            slow += 1
        return -1

        

        