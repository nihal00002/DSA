class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def function(index, subset):
            if index >= len(nums):
                result.append(subset[:])
                return 
            subset.append(nums[index])
            function(index + 1, subset)
            subset.pop()
            function(index + 1, subset)
        function(0,[])
        return result 