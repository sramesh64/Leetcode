class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False] * len(nums)
        res = []
        curr = []

        def dfs(used):
            if(False not in used):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if(used[i] == False):
                    curr.append(nums[i])
                    used[i] = True
                    dfs(used)
                    curr.pop()
                    used[i] = False
        
                    
        dfs(used)

        return res


        
