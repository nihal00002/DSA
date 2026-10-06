class Solution:
	def subsetSums(self, arr):
	    # code here
		result = []
		def solve(index,total):
		    if index >= len(arr):
		        result.append(total)
		        return 
		    total += arr[index]
		    solve(index + 1, total)
		    total -= arr[index]
		    solve(index + 1, total)
		    return result 
		return solve(0,0)
		        