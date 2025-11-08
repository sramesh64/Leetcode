class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []

        curr_string = ""

        def dfs(curr_string, num_opened, num_closed):
            if(num_closed > num_opened or num_opened > n or num_closed > n):
                return
            if(num_opened == n and num_closed == n):
                res.append(curr_string)
                return

            dfs(curr_string + "(", num_opened + 1, num_closed)
            dfs(curr_string + ")", num_opened, num_closed + 1)
            return

        dfs(curr_string, 0, 0)

        return res