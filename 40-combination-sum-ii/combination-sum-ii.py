class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        curr = []
        res = []
        def dfs(index, curr_sum):
            if(curr_sum == target):
                res.append(curr[:])
                return
            if(curr_sum > target or index == len(candidates)):
                return
            
            num = candidates[index]

            curr.append(num)
            dfs(index + 1, curr_sum + num)
            curr.pop()
            
            j = index + 1
            while j < len(candidates) and candidates[j] == num:
                j += 1
            dfs(j, curr_sum)

        dfs(0, 0)

        return res