class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=maxsum=nums[0]
        for i in range(1,len(nums)):
            if maxsum>0:
                maxsum+=nums[i]                
            else:
                maxsum=nums[i]
            res=max(res,maxsum)
        return res
