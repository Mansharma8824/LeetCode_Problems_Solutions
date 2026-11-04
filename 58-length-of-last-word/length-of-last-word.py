class Solution(object):
    def lengthOfLastWord(self, s):
        string = s.strip()
        last = len(string)-1
        count = 0 
        while last >= 0 and  string[last] != " ":
                count +=1 
                last -= 1
                
        return count