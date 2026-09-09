class Solution:
    def findUnion(self, a, b):
        # code here 
        j=i=0
        arr = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if len(arr) == 0 or arr[-1] != a[i]:
                    arr.append(a[i])
                i += 1
            else:
                if len(arr) == 0 or arr[-1] != b[j]:
                    arr.append(b[j])
                j += 1
        while i < len(a):
            if len(arr) == 0 or arr[-1] != a[i]:
                    arr.append(a[i])
            i += 1
        while j < len(b):
            if len(arr) == 0 or arr[-1] != b[j]:
                    arr.append(b[j])
            j += 1
        return arr
                