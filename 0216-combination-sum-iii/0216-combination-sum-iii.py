class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def solve(index,total,subset):

            if len(subset) == k and total == n:

                result.append(subset[:])

                return 

            if len(subset) > k or total > n:

                return

            for i in range(index,10):

                if total + i > n:

                    break

                subset.append(i)

                solve(i+1,total + i,subset)

                subset.pop()

            return result
            
        return solve(1,0,[])

            