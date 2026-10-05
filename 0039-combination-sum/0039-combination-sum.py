class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def function(index, total,subset):
            if total == target:
                result.append(subset[:])
                return 
            if index >= len(candidates):
                return 
            if total > target:
                return 
            total += candidates[index]
            subset.append(candidates[index])
            function(index,total,subset)
            e = subset.pop()
            total = total - e
            function(index + 1, total, subset)
            return result
        return function(0,0,[])
            
            
            
