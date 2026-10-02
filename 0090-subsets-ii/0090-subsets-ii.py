class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        def function(index,subset):
            if index >= len(nums):
                result.append(subset[:])
                return 
            subset.append(nums[index])
            function(index + 1, subset)
            subset.pop()
            while len(nums) > index + 1 and nums[index + 1] == nums[index]:
                index += 1
            function(index + 1, subset)
        function(0,[])
        return result