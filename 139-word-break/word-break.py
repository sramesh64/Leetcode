class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range (1, len(s) +1):
            for j in range(i):
                if(dp[j] and s[j:i] in words):
                    dp[i] = True

        return dp[len(s)]

