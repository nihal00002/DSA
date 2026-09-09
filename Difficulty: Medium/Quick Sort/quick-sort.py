class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low <high:
            p_idx = self.partition(arr,low,high)
            self.quickSort(arr,low,p_idx-1)
            self.quickSort(arr,p_idx + 1, high)
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low 
        j = high
        while i <j:
            while arr[i]<=pivot and i <= high -1:
                i += 1
            while arr[j]> pivot and j>=low +1:
                j -= 1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
            
                
            