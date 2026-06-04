class Solution:
    def minPathSum(self,matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]= matrix[i][j]
                    continue
                up = matrix[i][j]
                if i>0:
                    up +=dp[i-1][j]
                else:
                    up+= int(1e9)
                left= matrix[i][j]
                if j>0:
                    left += dp[i][j-1]
                else:
                    left += int(1e9)
                dp[i][j] = min(up,left)
        return dp[n-1][m-1]