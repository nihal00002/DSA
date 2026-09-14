class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        x_overlap = x1 < x4 and x3 < x2
        y_overlap = y1 < y4 and y3 < y2

        return x_overlap and y_overlap

