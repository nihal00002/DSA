class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        var1 = []
        var2 = []
        result = []
        for ele in nums:
            if ele > 0:
                var1.append(ele)
            else:
                var2.append(ele)
        count = 0
        while count < int(len(nums)/2):
            result.append(var1[count])
            result.append(var2[count])
            count +=1
        return result