class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        n=len(nums)
        max1= (nums[0]-1)*(nums[1]-1)
        max2 =(nums[n-1]-1)*(nums[n-2]-1)

        return max(max1,max2)
        