class Solution:
    def nextLargerElement(self, arr):
        # code here
        result = [-1] * len(arr)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result