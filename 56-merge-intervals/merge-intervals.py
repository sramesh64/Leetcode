class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals):
            if (i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]):
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])] 
                intervals.pop(i+1)
            else:
                i += 1

        return intervals