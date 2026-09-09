class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []
        count = 0
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
            else:
                count += 1
        for j in range(count):
            temp.append(0)
        for k in range(len(temp)):
            nums[k]=temp[k]
        return nums