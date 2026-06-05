class Solution:
    def helper(self,nums,current,used,result):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]= True
            current.append(nums[i])
            self.helper(nums,current,used,result)
            current.pop()
            used[i]=False
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False]*len(nums)
        self.helper(nums,[],used,result)
        return result
        