class Solution(object):
    def removeDuplicates(self, nums):
            s = 0
            f = 1
            while s < len(nums) and f < len(nums):
                if nums[f] != nums[s]:
                    s += 1
                    nums[s] = nums[f]
                    
                f += 1
                    
            return s+1

        