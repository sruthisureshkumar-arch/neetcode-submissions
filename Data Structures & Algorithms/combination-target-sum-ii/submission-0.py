class Solution:
    def findCombination(self,ans,ds,ind,target,arr):
        if target == 0:
            ans.append(list(ds))
            return
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.findCombination(ans,ds,i+1,target-arr[i],arr)
            ds.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        ds= []
        self.findCombination(ans,ds,0,target,candidates)
        return ans
        