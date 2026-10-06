class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,10)]
        result = []
        def solve(index,total,subset):
            if len(subset) == k and total == n:
                result.append(subset[:])
                return 
            if index >= len(nums):
                return 
            if total > n:
                return 
            subset.append(nums[index])
            total += nums[index]
            solve(index + 1, total, subset)
            e = subset.pop()
            total -= e 
            solve(index + 1,total,subset)
            return result
        return solve(0,0,[])

            