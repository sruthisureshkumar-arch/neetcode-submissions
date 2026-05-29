class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]
        low = nums[0]
        best = nums[0]
        for i in nums[1:]:
            vals = (i, curr * i, low * i)
            curr = max(vals)
            low = min(vals)
            best = max(best, curr)
        return best;
        