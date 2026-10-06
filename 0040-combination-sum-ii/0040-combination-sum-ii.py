class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def function(index, total, subset):

            if total == 0:
            
                result.append(subset[:])

                return 

            if index >= len(candidates) or total < 0:

                return 

            for i in range(index,len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:

                    continue

                if candidates[i]> total:

                    break

                subset.append(candidates[i])

                sum = total - candidates[i]

                function(i+1,sum,subset)

                subset.pop()

            return result 
            
        return function(0,target,[])