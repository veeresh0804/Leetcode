class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        
        option1 = nums[0] * nums[1] * nums[2]
        option2 = nums[-1] * nums[-2] * nums[0]
        
        return max(option1, option2)