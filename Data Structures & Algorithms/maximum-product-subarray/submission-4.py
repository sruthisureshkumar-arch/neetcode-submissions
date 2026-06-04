class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suff =1
        n = len(nums)
        ans = float('-inf')
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff=1
            pre *= nums[i]
            suff *= nums[n-i-1]
            ans = max(pre,suff,ans)
        return ans