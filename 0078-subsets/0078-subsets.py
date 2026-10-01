class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        number_of_subset = 1<<len(nums)
        result = []
        for i in range(number_of_subset):
            lst = []
            for j in range(len(nums)):
                if i & (1<<j) != 0:
                    lst.append(nums[j])
            result.append(lst)
        return result