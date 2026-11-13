class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = sorted(zip(val,wt),key = lambda x: x[0]/x[1],reverse=True)
        total =0.0
        for v,w in items:
            if capacity >= w:
                total += v
                capacity -= w
            else:
                total += v * (capacity/w)
                break
        return total