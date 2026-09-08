class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)-2,-1,-1):
            flag = False
            for j in range(i+1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    flag = True
            if flag == False:
                break
        return arr
        