class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        maxL= max(len(w) for w in wordDict)
        dp = [False]*(n+1)
        dp[n] = True
        for i in range(n-1,-1,-1):
            for j in range(i,min(i+maxL,n)):
                if dp[j+1]and s[i:j+1] in wordSet:
                    dp[i]= True
                    break
        return dp[0]