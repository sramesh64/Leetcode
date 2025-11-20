class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}

        def dfs(s_i, p_i):
            if ((s_i, p_i) in memo):
                return memo[(s_i, p_i)]


            if(s_i == len(s) and p_i == len(p)):
                memo[(s_i, p_i)] = True
                return True
            
            if(p_i == len(p) and s_i < len(s)):
                memo[(s_i, p_i)] = False
                return False
            
            if(p_i < len(p) - 1 and p[p_i + 1] == '*'):
                #dont use it
                if(dfs(s_i, p_i + 2)):
                    memo[(s_i, p_i)] = True
                    return True
                #use it
                if(s_i < len(s)):
                    if(s[s_i] == p[p_i] or p[p_i] == '.'):
                        if(dfs(s_i + 1, p_i)):
                            memo[(s_i, p_i)] = True
                            return True
                memo[(s_i, p_i)] = False
                return False

            if(s_i < len(s)):
                if(s[s_i] == p[p_i] or p[p_i] == '.'):
                    memo[(s_i, p_i)] = dfs(s_i + 1, p_i + 1)
                    return memo[(s_i, p_i)]
            memo[(s_i, p_i)] = False
            return False

        return dfs(0, 0)

                