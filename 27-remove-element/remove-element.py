class Solution(object):
    def removeElement(self, nums, val):
        first = 0 
        for second in range(len(nums)):
            if nums[second] != val:
                nums[first] = nums[second]
                first += 1

        return first



        