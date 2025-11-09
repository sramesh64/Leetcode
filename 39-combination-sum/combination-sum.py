class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        curr = []

        def findCombination(start, rem_target):
            
            if(rem_target < 0):
                return
            if(rem_target == 0):
                res.append(curr[:])
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                findCombination(i, rem_target - candidates[i])
                curr.pop()

        findCombination(0, target)
        return res
