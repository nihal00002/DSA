class Solution:
    def activitySelection(self, start, end):
        meet = sorted(zip(start, end), key=lambda x: x[1])
        count = 1
        last_time = meet[0][1]
        for s, e in meet[1:]:
            if s > last_time:
                count += 1
                last_time = e
        return count