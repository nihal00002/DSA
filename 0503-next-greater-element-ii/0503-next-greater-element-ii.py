class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []
        for i in range(2* len(nums)-1,-1,-1):
            while len(stack) != 0 and nums[i % len(nums)] >= stack[-1]:
                stack.pop()
            if i < len(nums):

                if len(stack) != 0:
                    result[i] = stack[-1]

            stack.append(nums[i%len(nums)])
        return result
        
