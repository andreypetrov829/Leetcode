class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[False] * (n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = True
        for i in range(1, m+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]

        # recurrence relation
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == '.'))
                else:
                    dp[i][j] = False

        return dp[m][n]