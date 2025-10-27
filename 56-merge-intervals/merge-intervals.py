class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if (not res):
                res.append([start, end])
            if(res[-1][1] >= start):
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res